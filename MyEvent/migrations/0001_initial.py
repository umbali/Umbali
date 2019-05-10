# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-19 11:44
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ipn', '0007_auto_20160219_1135'),
        ('Event', '0002_auto_20181219_1244'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPreOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.EventLive')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Event PreOrder',
                'verbose_name_plural': 'Event PreOrder(s)',
            },
        ),
        migrations.CreateModel(
            name='MyEventLive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(default=None, max_length=100, null=True)),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='myEventLiveEvent', to='Event.EventLive')),
                ('paypal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ipn.PayPalIPN')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='myEventLiveUser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'My Event Live',
                'verbose_name_plural': 'My Event Lives',
            },
        ),
    ]
