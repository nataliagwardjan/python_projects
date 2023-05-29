from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 64, blank = False)
    year = models.PositiveSmallIntegerField(blank = False, default = 2000)
    description = models.TextField(default = '')
    release = models.DateField(null = True, blank = True)
    imdb_rating = models.DecimalField(max_digits = 4, decimal_places = 2, blank = True, null = True)
    poster = models.ImageField(upload_to = 'posters', null = True, blank = True)

    def __str__(self):
        return self.title_with_year()

    def title_with_year(self):
        return f"{self.title} ({self.year})"