from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),

    # Album
    path('albums/', AlbumsPageView.as_view(), name='albums'),
    path('album/<slug:slug>/update', UpdateAlbumView.as_view(), name='update_album'),
    path('albums/<slug:slug>/', AlbumDetailView.as_view(), name='album_detail'),
    path('create/album/', AlbumCreateView.as_view(), name='create_album'),

    # Song
    path('song/<slug:slug>/', SongDetailView.as_view(), name='song_detail'),
    path('song/<slug:slug>/update', UpdateSongView.as_view(), name='update_song'),
    path('create/song/', SongCreateView.as_view(), name='create_song'),
    path('song/<slug:slug>/delete', SongDeleteView.as_view(), name='delete_song'),
    path('search/', SearchResultView.as_view(), name='search_result'),
]