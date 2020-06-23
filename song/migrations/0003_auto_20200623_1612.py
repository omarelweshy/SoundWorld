# Generated by Django 3.0.6 on 2020-06-23 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('song', '0002_remove_song_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment_update', to=settings.AUTH_USER_MODEL, verbose_name='last updated by'),
        ),
        migrations.AddField(
            model_name='song',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='song_create', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='song',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='song_update', to=settings.AUTH_USER_MODEL, verbose_name='last updated by'),
        ),
    ]