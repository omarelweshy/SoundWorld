from rest_framework import serializers
from song.models import *
from album.models import *

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'Type', 'song_file', 'cover', 'date',)

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('title', 'songs', 'cover', 'date',)