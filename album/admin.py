from django.contrib import admin
from .models import *

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)
    list_filter = ('author','date',)
    search_fields = ('title' , 'author', 'date',)