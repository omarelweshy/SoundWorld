from django.forms import ModelForm
from .models import *

class SongCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]
