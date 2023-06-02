from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Movie, MovieAdditionalInfo, Review, Actor
from .forms import MovieForm, MovieAdditionalInfoForm, ReviewForm, ActorForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, MovieSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


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
    movie_form = MovieForm(request.POST or None, request.FILES or None)
    additional_info_form = MovieAdditionalInfoForm(request.POST or None)

    if all((movie_form.is_valid(), additional_info_form.is_valid())):
        movie = movie_form.save(commit = False)
        additional_info = additional_info_form.save()

        movie.additional_info = additional_info
        movie.save()
        return redirect(all_movies)

    return render(request, 'movie_form.html', {'movie_form': movie_form, 'additional_info_form': additional_info_form, 'is_new': True})

@login_required
def update_movie(request, id):
    movie = get_object_or_404(Movie, pk = id) # od razu rozwiązuje nam problem 404 not found
    reviews = Review.objects.filter(movie = movie)
    actors = movie.actors.all()

    try:
        additional_info = MovieAdditionalInfo.object.get(movie = movie.id)
    except:
        additional_info = None

    movie_form = MovieForm(request.POST or None, request.FILES or None, instance = movie)
    additional_info_form = MovieAdditionalInfoForm(request.POST or None, instance = additional_info)
    review_form = ReviewForm(request.POST or None)

    if request.method == 'POST':
        if 'mark' in request.POST:
            review = review_form.save(commit = False)
            review.movie = movie
            review.save()

    if all((movie_form.is_valid(), additional_info_form.is_valid())):
        movie = movie_form.save(commit = False)
        additional_info = additional_info_form.save()

        movie.additional_info = additional_info
        movie.save()
        return redirect(all_movies)

    return render(request, 'movie_form.html', {'movie_form': movie_form, 'additional_info_form': additional_info_form,
                                               'reviews': reviews, 'review_form': review_form, 'actors' : actors,
                                               'is_new': False})

@login_required
def remove_movie(request, id):
    movie = get_object_or_404(Movie, pk = id)  # od razu rozwiązuje nam problem 404 not found

    if request.method == 'POST':
        movie.delete()
        return redirect(all_movies)

    return render(request, 'confirm.html', {'movie': movie})
