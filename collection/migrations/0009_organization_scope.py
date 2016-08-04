# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0008_auto_20160803_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='scope',
            field=models.IntegerField(choices=[(0, 'closed'), (1, 'local'), (2, 'regional'), (3, 'national'), (4, 'international')], default=1, help_text='What is the level of influence, reach, or exposure of this Organization?'),
        ),
    ]
