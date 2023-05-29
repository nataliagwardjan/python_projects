from django.urls import path
from movies_web.views import all_movies, create_new_movie, update_movie, remove_movie

urlpatterns = [
    path('movies/', all_movies, name = 'get_all_movies'),
    path('create_new/', create_new_movie, name = 'add_new_movie'),
    path('update/<int:id>/', update_movie, name = 'update_movie'),
    path('remove/<int:id>', remove_movie, name = 'remove_movie')
]
