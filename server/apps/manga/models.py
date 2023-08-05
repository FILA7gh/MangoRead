from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'genre'
        verbose_name_plural = 'genres'


class Manga(models.Model):
    image = models.ImageField(upload_to='manga_image')
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    year = models.DateField()
    sinopsis = models.TextField()

    genres = models.ManyToManyField(Genre, related_name='manga_genre')

    class Meta:
        ordering = ['id']
        verbose_name = 'manga'
        verbose_name_plural = 'manga'

    def __str__(self):
        return self.title
