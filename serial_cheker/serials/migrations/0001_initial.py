# Generated by Django 4.0.4 on 2022-05-12 20:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Platforms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Serials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('budget', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('box_office', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('slug', models.SlugField(max_length=255)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serials.platforms')),
            ],
        ),
    ]