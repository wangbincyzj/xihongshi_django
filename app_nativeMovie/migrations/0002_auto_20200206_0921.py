# Generated by Django 2.2.9 on 2020-02-06 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_nativeMovie', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nativemovie',
            old_name='Scene',
            new_name='scene',
        ),
    ]
