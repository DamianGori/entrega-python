# Generated by Django 4.1.7 on 2023-04-11 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_main_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main_user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='main_user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='main_avatar',
        ),
        migrations.DeleteModel(
            name='main_user',
        ),
    ]
