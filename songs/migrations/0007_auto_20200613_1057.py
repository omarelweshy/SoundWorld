# Generated by Django 3.0.6 on 2020-06-13 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0006_auto_20200613_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]