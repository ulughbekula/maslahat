# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('author', models.TextField()),
                ('link', models.TextField()),
                ('type', models.TextField()),
                ('published', models.DateTimeField()),
                ('reactions', models.IntegerField()),
                ('comments', models.IntegerField()),
                ('shares', models.IntegerField()),
                ('likes', models.IntegerField()),
                ('loves', models.IntegerField()),
                ('wows', models.IntegerField()),
                ('hahas', models.IntegerField()),
                ('sads', models.IntegerField()),
                ('angrys', models.IntegerField()),
            ],
        ),
    ]
