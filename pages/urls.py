from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('albums/', AlbumsPageView.as_view(), name='albums'),
    path('songs/<slug:slug>/', SongDetailView.as_view(), name='song_detail'),
    path('albums/<slug:slug>/', AlbumDetailView.as_view(), name='album_detail'),
    path('song/<slug:slug>/update', UpdateSongView.as_view(), name='update_song'),
    path('album/<slug:slug>/update', UpdateAlbumView.as_view(), name='update_album'),
]