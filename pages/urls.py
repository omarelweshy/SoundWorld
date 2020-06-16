from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('albums/', AlbumsPageView.as_view(), name='albums'),
    path('song/<slug:slug>/', SongDetailView.as_view(), name='song_detail'),
    path('album/<slug:slug>/', AlbumDetailView.as_view(), name='album_detail'),
    path('song/<slug:slug>/update', UpdateSongView.as_view(), name='update_song')

]