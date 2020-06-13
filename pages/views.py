from django.views.generic import *
from songs.models import *

class HomePageView(ListView):
    model = Song
    context_object_name = 'song_list'
    template_name = 'home.html'

class AlbumsPageView(ListView):
    model = Album
    context_object_name = 'albums_list'
    template_name = 'albums.html'