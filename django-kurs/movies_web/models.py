from django.db import models
class MovieAdditionalInfo(models.Model):
    GENRE = {
        (0, 'INNE'),
        (1, 'HORROR'),
        (2, 'COMEDY'),
        (3, 'SCI-FI'),
        (4, 'DRAMA'),
        (5, 'ROMANCE')
    }
    term_of_movie = models.PositiveSmallIntegerField(default = 0)
    genre = models.PositiveSmallIntegerField(default = 0, choices = GENRE)

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 64, blank = False)
    year = models.PositiveSmallIntegerField(blank = False, default = 2000)
    description = models.TextField(default = '')
    release = models.DateField(null = True, blank = True)
    imdb_rating = models.DecimalField(max_digits = 4, decimal_places = 2, blank = True, null = True)
    poster = models.ImageField(upload_to = 'posters', null = True, blank = True)
    additional_info = models.OneToOneField(MovieAdditionalInfo, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.title_with_year()

    def title_with_year(self):
        return f"{self.title} ({self.year})"

class Review(models.Model):
    review_description = models.TextField(default = "", blank = True)
    mark = models.PositiveSmallIntegerField(default = 5)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)