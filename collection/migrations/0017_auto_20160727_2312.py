# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0016_auto_20160727_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='altnameattr',
            name='name',
            field=models.CharField(help_text='What other names was the item known by?', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(help_text='Work from the general to the specific, e.g. <em>last-name-first-name</em>.', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(help_text='Provide a title.', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(help_text='Provide a name for this Color, e.g. <em>scarlet</em> or <em>forest green</em>.', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='slug',
            field=models.SlugField(help_text='Work from the general to the specific, e.g. <em>last-name-first-name</em>.', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='emailattr',
            name='email',
            field=models.CharField(help_text='Provide an email address, e.g. <pre>allan@example.com</pre>.', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='identifierattr',
            name='identifier',
            field=models.CharField(help_text='An identifier from the original context, like a DOI, LoC, or museum accession number.', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='name',
            field=models.CharField(help_text='Provide a name for this License, e.g. <em>MIT license</em> or <em>Gnu Public License v. 2</em>.', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='slug',
            field=models.SlugField(help_text='Work from the general to the specific, e.g. <em>last-name-first-name</em>.', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='url',
            field=models.URLField(help_text='Provide a URL for the source of this License.', unique=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(help_text='Provide the canonical name for this Organization.', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='slug',
            field=models.SlugField(help_text='Work from the general to the specific, e.g. <em>last-name-first-name</em>.', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(help_text='Work from the general to the specific, e.g. <em>last-name-first-name</em>.', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='phoneattr',
            name='phone',
            field=models.CharField(help_text='Provide a phone number, e.g. <pre>(312) 987-6543</pre>', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='photograph',
            name='slug',
            field=models.SlugField(help_text='Work from the general to the specific, e.g. <em>last-name-first-name</em>.', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='photograph',
            name='title',
            field=models.CharField(help_text='Provide a title.', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='slug',
            field=models.SlugField(help_text='Work from the general to the specific, e.g. <em>last-name-first-name</em>.', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='title',
            field=models.CharField(help_text='Provide a title.', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='slug',
            field=models.SlugField(help_text='Work from the general to the specific, e.g. <em>last-name-first-name</em>.', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='title',
            field=models.CharField(help_text='Provide a title.', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='url',
            field=models.URLField(help_text='Provide the root URL for this Website, in the form <pre>http://example.com/</pre>.', unique=True),
        ),
    ]
