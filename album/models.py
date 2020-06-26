from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from autoslug import AutoSlugField
from django.urls import reverse
from song.models import Song
from author.decorators import with_author

@with_author
class Album(models.Model):   
    title = models.CharField(max_length=50)
    songs = models.ManyToManyField(Song, blank=True, related_name='song')
    slug = AutoSlugField(populate_from='title', unique=True)
    cover = models.ImageField(upload_to='album_cover', blank=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('album_detail', args=[str(self.slug)])