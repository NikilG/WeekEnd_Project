# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-08 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsfeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('by', models.CharField(max_length=256)),
                ('title', models.CharField(db_index=True, max_length=256)),
                ('type', models.CharField(max_length=256)),
                ('score', models.IntegerField()),
                ('url', models.DateField()),
                ('time', models.CharField(max_length=256)),
            ],
        ),
    ]
