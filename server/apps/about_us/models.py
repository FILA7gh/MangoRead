from django.db import models


class AboutUs(models.Model):
    tagline = models.CharField(max_length=255, blank=True)
    link_one = models.URLField(blank=True)
    link_two = models.URLField(blank=True)
    link_three = models.URLField(blank=True)
    map = models.URLField(blank=True)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'about us'
