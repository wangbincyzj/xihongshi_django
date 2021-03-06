# Generated by Django 2.2.9 on 2020-01-31 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(choices=[(0, '未删除'), (1, '已删除')], default=0, verbose_name='删除标识')),
                ('role_name', models.CharField(max_length=16, unique=True)),
                ('role_desc', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(choices=[(0, '未删除'), (1, '已删除')], default=0, verbose_name='删除标识')),
                ('account', models.CharField(max_length=16)),
                ('username', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64, null=True)),
                ('avatar', models.FileField(null=True, upload_to='')),
                ('token', models.CharField(max_length=64)),
                ('user_role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_user.Role')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
