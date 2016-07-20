# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 05:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0016_auto_20160720_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='dateattr',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.Work'),
        ),
        migrations.AddField(
            model_name='dateattr',
            name='source_accessed',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='descriptionattr',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.Work'),
        ),
        migrations.AddField(
            model_name='descriptionattr',
            name='source_accessed',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
