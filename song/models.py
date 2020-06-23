from django.db import models
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField
from django.urls import reverse
from django.conf import settings
from author.decorators import with_author

@with_author
class Song(models.Model):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title', unique=True)
    Type = models.CharField(max_length=50)
    song_file = models.FileField(upload_to='songs', blank=False)
    cover = models.ImageField(upload_to='song_cover', default='song_cover/default.jpg')
    date = models.DateField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('song_detail', args=[str(self.slug)])

@with_author
class Comment(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE,
            related_name='comments')
    comment = models.CharField(max_length=225)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('song_detail', args=[str(self.slug)])
    