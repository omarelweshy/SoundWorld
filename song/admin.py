from django.contrib import admin
from .models import *

class CommentInline(admin.TabularInline):
    model = Comment

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    
    list_display = ('title', 'Type',)
    list_filter = ('Type', 'date')
    search_fields = ('title', 'Type',)