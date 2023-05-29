from django.urls import path
from movies_web.views import all_movies

urlpatterns = [
    path('movies/', all_movies)
]
