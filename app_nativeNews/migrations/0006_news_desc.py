# Generated by Django 2.2.9 on 2020-02-02 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_nativeNews', '0005_remove_news_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='desc',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
