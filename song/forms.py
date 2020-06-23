from django.forms import ModelForm
from .models import *

class SongCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]

# class CreateSongForm(ModelForm):
#     class Meta:
#         model = Song
#         fields = ['title', 'Type', 'song_file', 'cover', 'date',]
