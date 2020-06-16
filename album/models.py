from django.db import models
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField
from song.models import *

class Album(models.Model):
    author = models.ForeignKey(get_user_model(),
        on_delete=models.CASCADE,
    )    
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title', unique=True)
    cover = models.ImageField(upload_to='album_cover', blank=False)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='song', blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title