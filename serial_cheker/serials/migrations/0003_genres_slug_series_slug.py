# Generated by Django 4.0.4 on 2022-05-18 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serials', '0002_series'),
    ]

    operations = [
        migrations.AddField(
            model_name='genres',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='series',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
