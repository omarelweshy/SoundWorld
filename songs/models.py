from django.db import models
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField

class Song(models.Model):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title', unique=True)
    Type = models.CharField(max_length=50)
    song_file = models.FileField(upload_to='songs', blank=False)
    cover = models.ImageField(upload_to='song_cover', default='song_cover/default.jpg')
    author = models.ForeignKey(get_user_model(),
        on_delete=models.CASCADE,
    )    
    date = models.DateField()

    def __str__(self):
        return self.title

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