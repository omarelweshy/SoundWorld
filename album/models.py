from django.db import models
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField
from song.models import Song

class Album(models.Model):
    author = models.ForeignKey(get_user_model(),
        on_delete=models.CASCADE,
    )    
    title = models.CharField(max_length=50)
    songs = models.ManyToManyField(Song, blank=True, null=True, related_name='song')
    slug = AutoSlugField(populate_from='title', unique=True)
    cover = models.ImageField(upload_to='album_cover', blank=False)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('song_detail', args=[str(self.slug)])