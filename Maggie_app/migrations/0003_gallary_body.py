# Generated by Django 2.2.14 on 2024-02-25 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maggie_app', '0002_auto_20240225_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallary',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]
