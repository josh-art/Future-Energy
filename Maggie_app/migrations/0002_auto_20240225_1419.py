# Generated by Django 2.2.14 on 2024-02-25 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Maggie_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post_connected',
        ),
        migrations.RemoveField(
            model_name='favourites',
            name='post',
        ),
        migrations.RemoveField(
            model_name='favourites',
            name='user',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='post',
            name='favourite',
        ),
        migrations.RemoveField(
            model_name='post',
            name='liked',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Favourites',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
