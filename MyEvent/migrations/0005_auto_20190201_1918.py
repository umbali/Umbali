# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-01 19:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyEvent', '0004_auto_20190131_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myeventlive',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myEventLiveEvent', to='Event.EventLive'),
        ),
        migrations.AlterField(
            model_name='myeventlive',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myEventLiveUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
