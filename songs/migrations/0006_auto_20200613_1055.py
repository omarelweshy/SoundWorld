# Generated by Django 3.0.6 on 2020-06-13 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0005_auto_20200613_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date',
            field=models.DateField(blank=True),
        ),
    ]
