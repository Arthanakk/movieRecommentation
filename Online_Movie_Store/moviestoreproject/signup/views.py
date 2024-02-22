from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid login')
    else:
        return render(request, 'login.html')
# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        Firstname=request.POST['First_name']
        Lastname=request.POST['Last_name']
        email=request.POST['emailid']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=Firstname, last_name=Lastname, email=email,
                                                password=password)
                user.save()
                print("user registered")
                return redirect('login')

        else:
            messages.info(request,"password not match")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,"signup.html")
def logout(request):
    auth.logout(request)
    return redirect('/')