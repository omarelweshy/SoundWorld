from django.views.generic import *
from song.models import *
from album.models import *
from django.views.generic.edit import UpdateView
from song.forms import *
from django.urls import reverse
from django.shortcuts import redirect

class HomePageView(ListView):
    model = Song
    context_object_name = 'song_list'
    template_name = 'home.html'

class AlbumsPageView(ListView):
    model = Album
    context_object_name = 'albums_list'
    template_name = 'albums.html'

class SongDetailView(DetailView):
    model = Song
    context_object_name = 'song'
    template_name = "song_detail.html"

class AlbumDetailView(DetailView):
    model = Album
    context_object_name = 'albums_list'
    template_name = "album_detail.html"

class UpdateSongView(UpdateView):
    model = Song
    fields = ['title', 'Type', 'song_file', 'cover', 'date',]
    context_object_name = 'song'
    template_name = 'forms/update_song_form.html'

