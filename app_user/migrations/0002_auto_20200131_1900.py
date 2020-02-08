# Generated by Django 2.2.9 on 2020-01-31 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='account',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='nickname',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
