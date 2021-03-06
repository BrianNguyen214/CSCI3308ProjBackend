# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-12-03 23:05
from __future__ import unicode_literals

from django.db import migrations, models
import event.tokens


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_auto_20181130_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='token1',
            field=models.IntegerField(default=event.tokens.GetToken1),
        ),
        migrations.AddField(
            model_name='event',
            name='token2',
            field=models.IntegerField(default=event.tokens.GetToken2),
        ),
        migrations.AddField(
            model_name='event',
            name='token3',
            field=models.CharField(default=event.tokens.GetToken3, max_length=1000),
        ),
    ]
