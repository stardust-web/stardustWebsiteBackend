# Generated by Django 2.0.4 on 2021-06-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Research', '0003_auto_20210617_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researchpaper',
            name='file',
        ),
        migrations.AddField(
            model_name='researchpaper',
            name='pdf_link',
            field=models.URLField(default='None'),
        ),
    ]
