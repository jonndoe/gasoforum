# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-03 17:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20180303_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastopic',
            name='avatar',
            field=models.ImageField(upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 3, 17, 14, 58, 701644, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='photoalbum',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 3, 17, 14, 58, 701644, tzinfo=utc)),
        ),
    ]