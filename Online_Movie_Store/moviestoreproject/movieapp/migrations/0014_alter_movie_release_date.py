# Generated by Django 4.2.8 on 2024-02-22 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0013_alter_movie_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(),
        ),
    ]