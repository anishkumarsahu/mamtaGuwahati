# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-10-12 11:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mamtaApp', '0008_auto_20191012_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='isDeleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='company',
            name='lastUpdatedOn',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
