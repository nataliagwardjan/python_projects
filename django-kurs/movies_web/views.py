from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.
def all_movies(request):
    # return HttpResponse('This is our first test')
    movies_list = Movie.objects.all()
    return render(request, 'movies.html', {'movies': movies_list})

