# Generated by Django 4.2.8 on 2024-02-20 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='slug',
        ),
    ]
