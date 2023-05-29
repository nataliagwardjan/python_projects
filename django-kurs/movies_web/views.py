from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def all_movies(request):
    # return HttpResponse('This is our first test')
    movies_list = Movie.objects.all()
    return render(request, 'movies.html', {'movies' : movies_list})

@login_required
def get_movie_by_id(request):
    movie = Movie.objects.get(id = 1)
    return render(request, 'movies.html', {'movie_by_id' : movie})

@login_required
def get_movie_by_filter(request):
    movie = Movie.objects.filter(id = 1)
    return render(request, 'movies.html', {'movie_by_filter': movie})

@login_required
def create_new_movie(request):
    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(all_movies)

    return render(request, 'movie_form.html', {'form': form})

@login_required
def update_movie(request, id):
    movie = get_object_or_404(Movie, pk = id) # od razu rozwiązuje nam problem 404 not found
    form = MovieForm(request.POST or None, request.FILES or None, instance = movie)
    if form.is_valid():
        form.save()
        return redirect(all_movies)

    return render(request, 'movie_form.html', {'form': form})

@login_required
def remove_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)  # od razu rozwiązuje nam problem 404 not found

    if request.method == 'POST':
        movie.delete()
        return redirect(all_movies)

    return render(request, 'confirm.html', {'movie': movie})
