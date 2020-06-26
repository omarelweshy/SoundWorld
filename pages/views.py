from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from song.models import *
from album.models import *
from django.views.generic.edit import UpdateView, CreateView
from song.forms import *
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

class HomePageView(ListView):
    model = Song
    context_object_name = 'song_list'
    template_name = 'home.html'

class AlbumsPageView(ListView):
    model = Album
    context_object_name = 'albums_list'
    template_name = 'albums.html'

class SongDetailView(LoginRequiredMixin, DetailView):
    model = Song
    context_object_name = 'song'
    template_name = "song_detail.html"
    login_url = "account_login"

class AlbumDetailView(LoginRequiredMixin, DetailView):
    model = Album
    context_object_name = 'album'
    template_name = "album_detail.html"
    login_url = "account_login"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['song_list'] = Song.objects.select_related('song').all()
    #     return context

class UpdateSongView(LoginRequiredMixin, UpdateView):
    model = Song
    fields = ['title', 'Type', 'song_file', 'cover', 'date',]
    context_object_name = 'song'
    template_name = 'forms/update_song_form.html'
    login_url = "account_login"

class UpdateAlbumView(LoginRequiredMixin, UpdateView):
    model = Album
    fields = ['title', 'songs', 'cover', 'date',]
    context_object_name = 'album'
    template_name = 'forms/update_album_form.html'
    login_url = "account_login"

class SongCreateView(LoginRequiredMixin, CreateView):
    model = Song
    template_name = "forms/create_song_form.html"
    fields = ['title', 'Type', 'song_file', 'cover', 'date',]
    login_url = "account_login"

class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['title', 'songs', 'cover', 'date',]
    template_name = "forms/create_album_form.html"
    login_url = "account_login"

class SongDeleteView(LoginRequiredMixin, DeleteView):
    model = Song
    context_object_name = 'song'
    template_name = "forms/song_confirm_delete.html"
    success_url = reverse_lazy('home')
    login_url = "account_login"

class SearchResultView(ListView):
    model = Song
    context_object_name = 'song_list'
    template_name = "search_result.html"
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Song.objects.filter(
        Q(title__icontains=query) | Q(Type__icontains=query)
        )
