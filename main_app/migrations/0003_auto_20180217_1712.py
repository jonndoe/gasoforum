# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-17 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_gastheme_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastopictext',
            name='order',
            field=models.CharField(default='1', max_length=3),
        ),
        migrations.AlterField(
            model_name='gastopictext',
            name='subtitle',
            field=models.CharField(default='no', max_length=50),
        ),
        migrations.AlterField(
            model_name='gastopictext',
            name='text',
            field=models.TextField(default='текст абзаца'),
        ),
        migrations.AlterField(
            model_name='gastopictext',
            name='title',
            field=models.CharField(default='no', max_length=50),
        ),
    ]
