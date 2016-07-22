# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 20:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_auto_20160722_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrgPersonRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('EMPLOYEE', 'Department')], default='EMPLOYEE', max_length=50)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.Person')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.Organization')),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='related_people',
            field=models.ManyToManyField(through='collection.OrgPersonRelationship', to='collection.Person'),
        ),
    ]
