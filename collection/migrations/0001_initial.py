# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 19:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Item Name', max_length=200)),
                ('slug', models.SlugField(default='item-name', max_length=200)),
                ('hue', models.DecimalField(decimal_places=3, max_digits=6)),
                ('saturation', models.DecimalField(decimal_places=3, max_digits=6)),
                ('lightness', models.DecimalField(decimal_places=3, max_digits=6)),
                ('alpha', models.DecimalField(decimal_places=3, max_digits=4)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DateAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveIntegerField(default=0)),
                ('source_accessed', models.DateField(default=django.utils.timezone.now)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField(blank=True, null=True)),
                ('day', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DescriptionAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveIntegerField(default=0)),
                ('source_accessed', models.DateField(default=django.utils.timezone.now)),
                ('body', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Item Name', max_length=200)),
                ('slug', models.SlugField(default='item-name', max_length=200)),
                ('date_begin', models.ForeignKey(blank=True, default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='collection_organization_begin', to='collection.DateAttr')),
                ('date_end', models.ForeignKey(blank=True, default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='collection_organization_end', to='collection.DateAttr')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Item Name', max_length=200)),
                ('slug', models.SlugField(default='item-name', max_length=200)),
                ('name_last', models.CharField(max_length=200)),
                ('name_first', models.CharField(blank=True, max_length=200)),
                ('date_begin', models.ForeignKey(blank=True, default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='collection_person_begin', to='collection.DateAttr')),
                ('date_end', models.ForeignKey(blank=True, default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='collection_person_end', to='collection.DateAttr')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Item Name', max_length=200)),
                ('slug', models.SlugField(default='item-name', max_length=200)),
                ('url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Item Name', max_length=200)),
                ('slug', models.SlugField(default='item-name', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='descriptionattr',
            name='source',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='collection.Source'),
        ),
        migrations.AddField(
            model_name='dateattr',
            name='source',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='collection.Source'),
        ),
    ]
