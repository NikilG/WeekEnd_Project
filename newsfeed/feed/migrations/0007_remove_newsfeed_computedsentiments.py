# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-10 07:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_newsfeed_computedsentiments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsfeed',
            name='computedsentiments',
        ),
    ]
