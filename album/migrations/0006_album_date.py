# Generated by Django 3.0.6 on 2020-06-19 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0005_remove_album_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]