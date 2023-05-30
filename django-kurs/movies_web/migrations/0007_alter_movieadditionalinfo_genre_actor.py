# Generated by Django 4.2.1 on 2023-05-30 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_web', '0006_alter_movieadditionalinfo_genre_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieadditionalinfo',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(2, 'COMEDY'), (3, 'SCI-FI'), (5, 'ROMANCE'), (4, 'DRAMA'), (0, 'INNE'), (1, 'HORROR')], default=0),
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='John', max_length=32)),
                ('lastname', models.CharField(default='Smith', max_length=32)),
                ('movies', models.ManyToManyField(to='movies_web.movie')),
            ],
        ),
    ]