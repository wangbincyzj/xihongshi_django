# Generated by Django 2.2.9 on 2020-02-05 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_mall', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mall',
            name='username',
        ),
    ]
