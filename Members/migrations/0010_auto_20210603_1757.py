# Generated by Django 2.0.4 on 2021-06-03 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0009_auto_20210603_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='linkedin',
            field=models.URLField(null=True),
        ),
    ]
