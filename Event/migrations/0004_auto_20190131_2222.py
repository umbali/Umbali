# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-31 21:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0003_auto_20190124_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventlivecommentconf',
            name='event',
        ),
        migrations.RemoveField(
            model_name='eventlivestreamconf',
            name='application',
        ),
        migrations.RemoveField(
            model_name='eventlivestreamconf',
            name='disable_authentication',
        ),
        migrations.RemoveField(
            model_name='eventlivestreamconf',
            name='host_port',
        ),
        migrations.RemoveField(
            model_name='eventlivestreamconf',
            name='password',
        ),
        migrations.RemoveField(
            model_name='eventlivestreamconf',
            name='primary_server',
        ),
        migrations.RemoveField(
            model_name='eventlivestreamconf',
            name='stream_name',
        ),
        migrations.RemoveField(
            model_name='eventlivestreamconf',
            name='username',
        ),
        migrations.DeleteModel(
            name='EventLiveCommentConf',
        ),
    ]
