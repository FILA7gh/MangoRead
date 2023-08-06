from django.db import models
from django.contrib.auth.models import User
from avatar.models import Avatar

from server.apps.manga.models import Manga


class Review(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, null=True)
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review')
    text = models.TextField()

    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'reviews'

    def __str__(self):
        return f'{self.user.username} {self.manga.title}'
