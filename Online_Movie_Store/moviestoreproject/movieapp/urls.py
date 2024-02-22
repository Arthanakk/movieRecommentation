from django.urls import path
from.import views
app_name='movieapp'
urlpatterns = [

    path('',views.allMovCat,name='allMovCat'),
    path('<int:c_id>/',views.allMovCat,name='movie_by_category'),
    path('<int:c_id>/<str:m_id>/',views.MovieDetail,name='movieCatDeatil'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),

]

