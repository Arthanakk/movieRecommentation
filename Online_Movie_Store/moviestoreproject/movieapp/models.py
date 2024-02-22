from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    # slug = models.SlugField(max_length=250, unique=True)
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def get_url(self):
        return reverse('movieapp:movie_by_category',args=[str(self.id)])

    def __str__(self):
        return '{}'.format(self.name)
class Movie(models.Model):
    name=models.CharField(max_length=250,unique=True)
    # slug = models.SlugField(max_length=250, unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='movieimage',blank=True)
    language=models.CharField(max_length=250)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    release_date=models.DateField()
    release_date=models.DateField()
    actor=models.CharField(max_length=200)
    trailer=models.URLField(max_length=500)
    added_by=models.ForeignKey(User, on_delete=models.CASCADE)
    def get_url(self):
        return reverse('movieapp:movieCatDeatil',args=[self.category.id,self.id])
    class Meta:
        ordering=('name',)
        verbose_name='movie'
        verbose_name_plural='movies'
    def __str__(self):
        return '{}'.format(self.name)
class UserProfile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField( validators=[MaxValueValidator(5)])
    comment = models.TextField()
    created_by = models.ForeignKey(User, related_name='reviews_created', on_delete=models.CASCADE)