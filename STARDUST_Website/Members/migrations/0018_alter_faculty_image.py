# Generated by Django 3.2.4 on 2021-06-30 07:52

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0017_auto_20210630_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
