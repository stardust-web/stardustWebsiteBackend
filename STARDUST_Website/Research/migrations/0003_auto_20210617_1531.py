# Generated by Django 2.0.4 on 2021-06-17 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Research', '0002_auto_20210403_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchpaper',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='research/'),
        ),
    ]
