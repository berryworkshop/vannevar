# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_auto_20160713_0622'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='name_first',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='name_last',
            field=models.CharField(default='Example', max_length=200),
            preserve_default=False,
        ),
    ]
