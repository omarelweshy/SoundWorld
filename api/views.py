from rest_framework import generics, permissions
from song.models import *
from album.models import *
from .serializers import *

class SongListAPIView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'slug'

class SongCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class AlbumListAPIView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    lookup_field = 'slug'