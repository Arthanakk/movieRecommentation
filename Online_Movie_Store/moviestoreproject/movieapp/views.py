from django.shortcuts import render,get_object_or_404,redirect
from .models import Category,Movie,Review
from .forms import MovieForm
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def allMovCat(request,c_id=None):
    c_page=None
    movies_list=None
    if c_id!=None:
        c_page=get_object_or_404(Category,id=c_id)
        movies_list=Movie.objects.all().filter(category=c_page)
    else:
        movies_list=Movie.objects.all()
    paginator=Paginator(movies_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        movies=paginator.page(page)
    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_pages)


    return render(request, "category.html", {'category': c_page, 'movies': movies})

@login_required
def MovieDetail(request,m_id,c_id):
    try:
        movie=Movie.objects.get(category__id=c_id,id=m_id)
    except Exception as e:
        raise e
    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.created_by = request.user  # Set the created_by field
            review.save()
            return redirect('movieapp:movieCatDeatil', c_id=c_id, m_id=m_id)
    else:
        form = ReviewForm()

    reviews = Review.objects.filter(movie=movie)
    context = {
        'movie': movie,
        'form': form,
        'reviews': reviews,
        'c_id': movie.category.id,  # Replace with the actual category ID
        'm_id': movie.id,  # Replace with the actual movie ID
    }

    # Render the template with the created context
    return render(request, 'movie.html', context)

    # return render(request, 'movie.html', {'movie': movie, 'form': form, 'reviews': reviews})
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.added_by = request.user
            movie.save()
            return redirect('/')
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})
def update(request, id):
    movie = get_object_or_404(Movie,id=id)

    # Check if the user trying to edit is the one who added the movie
    if request.user != movie.added_by:
        messages.error(request, 'You do not have permission to edit this movie.')
        return redirect('/')

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'update.html', {'form': form, 'movie': movie})



def delete(request, id):
    movie = get_object_or_404(Movie, id=id)

    # Check if the user trying to delete is the one who added the movie
    if request.user != movie.added_by:
        messages.error(request, 'You do not have permission to delete this movie.')
        return redirect('/')

    movie.delete()
    messages.success(request, 'Movie deleted successfully.')
    return redirect('/')
