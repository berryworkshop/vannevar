# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0006_auto_20160719_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='source',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='source',
            name='object_id',
        ),
        migrations.AddField(
            model_name='dateattr',
            name='source',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='collection.Source'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='descriptionattr',
            name='source',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='collection.Source'),
            preserve_default=False,
        ),
    ]
