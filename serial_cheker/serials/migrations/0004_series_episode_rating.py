# Generated by Django 4.0.4 on 2022-05-18 22:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serials', '0003_genres_slug_series_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='episode_rating',
            field=models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
    ]
