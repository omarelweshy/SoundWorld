from django.forms import ModelForm
from .models import *

class CreateSongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'Type', 'song_file', 'cover', 'date',]
