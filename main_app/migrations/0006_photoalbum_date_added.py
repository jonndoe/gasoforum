# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-01 20:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_photoalbum'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoalbum',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 1, 20, 23, 32, 209171, tzinfo=utc)),
        ),
    ]
