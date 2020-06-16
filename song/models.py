from django.db import models
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse('song_detail', args=[str(self.slug)])