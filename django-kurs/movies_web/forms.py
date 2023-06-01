from django.forms import ModelForm
from .models import Movie, MovieAdditionalInfo, Review, Actor

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'description', 'release', 'imdb_rating', 'poster']

class MovieAdditionalInfoForm(ModelForm):
    class Meta:
        model = MovieAdditionalInfo
        fields = ['term_of_movie', 'genre']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review_description', 'mark']

class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = ['firstname', 'lastname', 'movies']
