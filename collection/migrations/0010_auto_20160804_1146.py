# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0009_organization_scope'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.TextField(blank=True, help_text='Provide the canonical physical address for this Organization.', null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='scope',
            field=models.IntegerField(choices=[(0, 'closed'), (1, 'local'), (2, 'regional'), (3, 'national'), (4, 'international')], default=2, help_text="What is the level of influence, reach, or exposure of this Organization within its industry?  This is a subjective rubric intended to imply scale or importance: an individual gallery, a supermarket, or a high school would be 'local'; a holding company, a city arts center, or a college would be 'regional'; most large corporations, museums, or state universities would be 'national'.  Only the largest, most famous entities, e.g. Microsoft, the Louvre, the New York Philharmonic, or Harvard University, are considered 'international'."),
        ),
        migrations.AlterField(
            model_name='organization',
            name='slug',
            field=models.SlugField(help_text='Work from the general to the specific, e.g. <em>last-name-first-name</em>.  If this is a generic name, affix with a parent acronym, e.g. <em>aic-prints-drawings</em>.', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='website',
            field=models.URLField(blank=True, help_text='Provide the canonical website URL for this Organization.', null=True),
        ),
        migrations.AlterField(
            model_name='organizationcategory',
            name='category',
            field=models.CharField(choices=[('ARCHIVE', 'archive'), ('ASSOCIATION', 'center'), ('CONSORTIUM', 'consortium'), ('CORPORATION', 'corporation'), ('FOUNDATION', 'foundation'), ('GALLERY', 'gallery'), ('LIBRARY', 'library'), ('MUSEUM', 'museum'), ('SCHOOL', 'school')], default='LIBRARY', help_text='What type of organization?', max_length=50, unique=True),
        ),
    ]
