# Generated by Django 4.2.8 on 2024-02-20 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_remove_category_slug_remove_movie_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]