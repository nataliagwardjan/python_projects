from django.contrib import admin
from .models import Movie, MovieAdditionalInfo

# Register your models here.
# First option
# admin.site.register(Movie)

# Second option
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['title'] # wybieramy pola, które chcemy używać
    # exclude = ['description'] # co mamy pomijać
    list_display = ['title', 'year'] # jak ma być wyświetlana lista obiektów
    list_filter = ['year'] # dodajemy filtr by wybrać np. tylko dany rok
    search_fields = ['title'] # dodajemy opcje szukania w tytule


admin.site.register(MovieAdditionalInfo)
