# Generated by Django 4.2.11 on 2024-03-18 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Maggie_app', '0003_gallary_body'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Advert',
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.RemoveField(
            model_name='messagemodel',
            name='recipient',
        ),
        migrations.RemoveField(
            model_name='messagemodel',
            name='user',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='post',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='to_user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='MessageModel',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
