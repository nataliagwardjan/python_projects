# Generated by Django 4.2.1 on 2023-05-28 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_web', '0003_movie_description_movie_imdb_rating_movie_poster_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb_rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
