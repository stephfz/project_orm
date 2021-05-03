from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    #path('movies', views.all_movies),
    path('movies/<int:director_id>', views.director_movies),
    path('movies', views.all_movies),
    path('movie', views.movie),
    path('director', views.director),
    path('genres', views.genres),
    path('genre/<int:genre_id>/movies', views.genre_movies),
]