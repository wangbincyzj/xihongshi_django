# Generated by Django 2.2.9 on 2020-02-06 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_nativeMovie', '0002_auto_20200206_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='nativemovie',
            name='username',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
