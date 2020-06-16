from django.forms import ModelForm
from .models import *

class UpdateSong(ModelForm):
    class Meta:
        Model = Song
        fields = ['title', 'Type', 'song_file', 'cover', 'date',]
