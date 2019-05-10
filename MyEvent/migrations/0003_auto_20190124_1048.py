# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-24 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyEvent', '0002_auto_20181219_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myeventlive',
            old_name='ip',
            new_name='buyer_ip',
        ),
        migrations.AddField(
            model_name='myeventlive',
            name='watcher_ip',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
