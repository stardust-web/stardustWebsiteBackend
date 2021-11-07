# Generated by Django 3.2.4 on 2021-06-30 07:52

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Achievements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
