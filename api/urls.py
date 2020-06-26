from django.urls import path
from .views import *

urlpatterns = [
    path('songs/', SongListAPIView.as_view()),
    path('songs/<slug:slug>/', SongDetailAPIView.as_view()),
    path('albums/', AlbumListAPIView.as_view()),
    path('albums/<slug:slug>/', AlbumDetailAPIView.as_view()),


]