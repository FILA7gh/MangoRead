from django.db import models
from django.contrib.auth.models import User
from avatar.models import Avatar


class Review(models.Model):
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review')
    text = models.TextField()

    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'reviews'

    def __str__(self):
        return self.user.username
