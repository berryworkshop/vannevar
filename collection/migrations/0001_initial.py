# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-31 14:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveIntegerField(default=0, help_text='Provide a display order.')),
                ('object_id', models.PositiveIntegerField(help_text='Provide the actual object ID of the generic relation within the table of the Content Type.')),
                ('source_accessed', models.DateField(blank=True, default=django.utils.timezone.now, help_text='When was this source consulted.')),
                ('category', models.CharField(choices=[('PRIMARY', 'primary'), ('SECONDARY', 'secondary'), ('WORK', 'work'), ('HOME', 'home'), ('INFODESK', 'main information desk')], default='PRIMARY', help_text='What type of postal address is this?', max_length=50)),
                ('street', models.TextField(help_text='Provide a street address.  For a new line, press <pre>shift-enter</pre> (<pre>shift-return</pre> on a Mac).')),
                ('city', models.CharField(help_text='Provide a city or community name.', max_length=100)),
                ('state_region', models.CharField(help_text='Provide a state, province, or other region for postal purposes.', max_length=100)),
                ('postal_code', models.CharField(help_text='Provide a zip or other postal code.', max_length=100)),
                ('country', models.CharField(choices=[('ABW', 'Aruba'), ('AFG', 'Afghanistan'), ('AGO', 'Angola'), ('AIA', 'Anguilla'), ('ALA', 'Åland Islands'), ('ALB', 'Albania'), ('AND', 'Andorra'), ('ARE', 'United Arab Emirates'), ('ARG', 'Argentina'), ('ARM', 'Armenia'), ('ASM', 'American Samoa'), ('ATA', 'Antarctica'), ('ATF', 'French Southern Territories'), ('ATG', 'Antigua and Barbuda'), ('AUS', 'Australia'), ('AUT', 'Austria'), ('AZE', 'Azerbaijan'), ('BDI', 'Burundi'), ('BEL', 'Belgium'), ('BEN', 'Benin'), ('BES', 'Bonaire, Sint Eustatius and Saba'), ('BFA', 'Burkina Faso'), ('BGD', 'Bangladesh'), ('BGR', 'Bulgaria'), ('BHR', 'Bahrain'), ('BHS', 'Bahamas'), ('BIH', 'Bosnia and Herzegovina'), ('BLM', 'Saint Barthélemy'), ('BLR', 'Belarus'), ('BLZ', 'Belize'), ('BMU', 'Bermuda'), ('BOL', 'Bolivia, Plurinational State of'), ('BRA', 'Brazil'), ('BRB', 'Barbados'), ('BRN', 'Brunei Darussalam'), ('BTN', 'Bhutan'), ('BVT', 'Bouvet Island'), ('BWA', 'Botswana'), ('CAF', 'Central African Republic'), ('CAN', 'Canada'), ('CCK', 'Cocos (Keeling) Islands'), ('CHE', 'Switzerland'), ('CHL', 'Chile'), ('CHN', 'China'), ('CIV', "Côte d'Ivoire"), ('CMR', 'Cameroon'), ('COD', 'Congo, the Democratic Republic of the'), ('COG', 'Congo'), ('COK', 'Cook Islands'), ('COL', 'Colombia'), ('COM', 'Comoros'), ('CPV', 'Cabo Verde'), ('CRI', 'Costa Rica'), ('CUB', 'Cuba'), ('CUW', 'Curaçao'), ('CXR', 'Christmas Island'), ('CYM', 'Cayman Islands'), ('CYP', 'Cyprus'), ('CZE', 'Czech Republic'), ('DEU', 'Germany'), ('DJI', 'Djibouti'), ('DMA', 'Dominica'), ('DNK', 'Denmark'), ('DOM', 'Dominican Republic'), ('DZA', 'Algeria'), ('ECU', 'Ecuador'), ('EGY', 'Egypt'), ('ERI', 'Eritrea'), ('ESH', 'Western Sahara'), ('ESP', 'Spain'), ('EST', 'Estonia'), ('ETH', 'Ethiopia'), ('FIN', 'Finland'), ('FJI', 'Fiji'), ('FLK', 'Falkland Islands (Malvinas)'), ('FRA', 'France'), ('FRO', 'Faroe Islands'), ('FSM', 'Micronesia, Federated States of'), ('GAB', 'Gabon'), ('GBR', 'United Kingdom'), ('GEO', 'Georgia'), ('GGY', 'Guernsey'), ('GHA', 'Ghana'), ('GIB', 'Gibraltar'), ('GIN', 'Guinea'), ('GLP', 'Guadeloupe'), ('GMB', 'Gambia'), ('GNB', 'Guinea-Bissau'), ('GNQ', 'Equatorial Guinea'), ('GRC', 'Greece'), ('GRD', 'Grenada'), ('GRL', 'Greenland'), ('GTM', 'Guatemala'), ('GUF', 'French Guiana'), ('GUM', 'Guam'), ('GUY', 'Guyana'), ('HKG', 'Hong Kong'), ('HMD', 'Heard Island and McDonald Islands'), ('HND', 'Honduras'), ('HRV', 'Croatia'), ('HTI', 'Haiti'), ('HUN', 'Hungary'), ('IDN', 'Indonesia'), ('IMN', 'Isle of Man'), ('IND', 'India'), ('IOT', 'British Indian Ocean Territory'), ('IRL', 'Ireland'), ('IRN', 'Iran, Islamic Republic of'), ('IRQ', 'Iraq'), ('ISL', 'Iceland'), ('ISR', 'Israel'), ('ITA', 'Italy'), ('JAM', 'Jamaica'), ('JEY', 'Jersey'), ('JOR', 'Jordan'), ('JPN', 'Japan'), ('KAZ', 'Kazakhstan'), ('KEN', 'Kenya'), ('KGZ', 'Kyrgyzstan'), ('KHM', 'Cambodia'), ('KIR', 'Kiribati'), ('KNA', 'Saint Kitts and Nevis'), ('KOR', 'Korea, Republic of'), ('KWT', 'Kuwait'), ('LAO', "Lao People's Democratic Republic"), ('LBN', 'Lebanon'), ('LBR', 'Liberia'), ('LBY', 'Libya'), ('LCA', 'Saint Lucia'), ('LIE', 'Liechtenstein'), ('LKA', 'Sri Lanka'), ('LSO', 'Lesotho'), ('LTU', 'Lithuania'), ('LUX', 'Luxembourg'), ('LVA', 'Latvia'), ('MAC', 'Macao'), ('MAF', 'Saint Martin (French part)'), ('MAR', 'Morocco'), ('MCO', 'Monaco'), ('MDA', 'Moldova, Republic of'), ('MDG', 'Madagascar'), ('MDV', 'Maldives'), ('MEX', 'Mexico'), ('MHL', 'Marshall Islands'), ('MKD', 'Macedonia, the former Yugoslav Republic of'), ('MLI', 'Mali'), ('MLT', 'Malta'), ('MMR', 'Myanmar'), ('MNE', 'Montenegro'), ('MNG', 'Mongolia'), ('MNP', 'Northern Mariana Islands'), ('MOZ', 'Mozambique'), ('MRT', 'Mauritania'), ('MSR', 'Montserrat'), ('MTQ', 'Martinique'), ('MUS', 'Mauritius'), ('MWI', 'Malawi'), ('MYS', 'Malaysia'), ('MYT', 'Mayotte'), ('NAM', 'Namibia'), ('NCL', 'New Caledonia'), ('NER', 'Niger'), ('NFK', 'Norfolk Island'), ('NGA', 'Nigeria'), ('NIC', 'Nicaragua'), ('NIU', 'Niue'), ('NLD', 'Netherlands'), ('NOR', 'Norway'), ('NPL', 'Nepal'), ('NRU', 'Nauru'), ('NZL', 'New Zealand'), ('OMN', 'Oman'), ('PAK', 'Pakistan'), ('PAN', 'Panama'), ('PCN', 'Pitcairn'), ('PER', 'Peru'), ('PHL', 'Philippines'), ('PLW', 'Palau'), ('PNG', 'Papua New Guinea'), ('POL', 'Poland'), ('PRI', 'Puerto Rico'), ('PRK', "Korea, Democratic People's Republic of"), ('PRT', 'Portugal'), ('PRY', 'Paraguay'), ('PSE', 'Palestine, State of'), ('PYF', 'French Polynesia'), ('QAT', 'Qatar'), ('REU', 'Réunion'), ('ROU', 'Romania'), ('RUS', 'Russian Federation'), ('RWA', 'Rwanda'), ('SAU', 'Saudi Arabia'), ('SDN', 'Sudan'), ('SEN', 'Senegal'), ('SGP', 'Singapore'), ('SGS', 'South Georgia and the South Sandwich Islands'), ('SHN', 'Saint Helena, Ascension and Tristan da Cunha'), ('SJM', 'Svalbard and Jan Mayen'), ('SLB', 'Solomon Islands'), ('SLD', 'Somaliland'), ('SLE', 'Sierra Leone'), ('SLV', 'El Salvador'), ('SMR', 'San Marino'), ('SOM', 'Somalia'), ('SPM', 'Saint Pierre and Miquelon'), ('SRB', 'Serbia'), ('SSD', 'South Sudan'), ('STP', 'Sao Tome and Principe'), ('SUR', 'Suriname'), ('SVK', 'Slovakia'), ('SVN', 'Slovenia'), ('SWE', 'Sweden'), ('SWZ', 'Swaziland'), ('SXM', 'Sint Maarten (Dutch part)'), ('SYC', 'Seychelles'), ('SYR', 'Syrian Arab Republic'), ('TCA', 'Turks and Caicos Islands'), ('TCD', 'Chad'), ('TGO', 'Togo'), ('THA', 'Thailand'), ('TJK', 'Tajikistan'), ('TKL', 'Tokelau'), ('TKM', 'Turkmenistan'), ('TLS', 'Timor-Leste'), ('TON', 'Tonga'), ('TTO', 'Trinidad and Tobago'), ('TUN', 'Tunisia'), ('TUR', 'Turkey'), ('TUV', 'Tuvalu'), ('TWN', 'Taiwan, Province of China'), ('TZA', 'Tanzania, United Republic of'), ('UGA', 'Uganda'), ('UKR', 'Ukraine'), ('UMI', 'United States Minor Outlying Islands'), ('URY', 'Uruguay'), ('USA', 'United States of America'), ('UZB', 'Uzbekistan'), ('VAT', 'Holy See (Vatican City State)'), ('VCT', 'Saint Vincent and the Grenadines'), ('VEN', 'Venezuela, Bolivarian Republic of'), ('VGB', 'Virgin Islands, British'), ('VIR', 'Virgin Islands, U.S.'), ('VNM', 'Viet Nam'), ('VUT', 'Vanuatu'), ('WLF', 'Wallis and Futuna'), ('WSM', 'Samoa'), ('YEM', 'Yemen'), ('ZAF', 'South Africa'), ('ZMB', 'Zambia'), ('ZWE', 'Zimbabwe')], default='USA', help_text='Select a nation or country.', max_length=3)),
                ('content_type', models.ForeignKey(help_text='Provide the model name for the generic relation.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'phones',
                'verbose_name': 'phone',
            },
        ),
        migrations.CreateModel(
            name='AltNameAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveIntegerField(default=0, help_text='Provide a display order.')),
                ('object_id', models.PositiveIntegerField(help_text='Provide the actual object ID of the generic relation within the table of the Content Type.')),
                ('source_accessed', models.DateField(blank=True, default=django.utils.timezone.now, help_text='When was this source consulted.')),
                ('name', models.CharField(help_text='What other names was the item known by?', max_length=200, unique=True)),
                ('content_type', models.ForeignKey(help_text='Provide the model name for the generic relation.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'names',
                'verbose_name': 'name',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('slug', models.SlugField(help_text='Work from the general to the specific, e.g. <em>last-name-first-name</em>.', max_length=200, unique=True)),
                ('title', models.CharField(help_text='Provide a title.', max_length=200, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('slug', models.SlugField(help_text='Work from the general to the specific, e.g. <em>last-name-first-name</em>.', max_length=200, unique=True)),
                ('name', models.CharField(help_text='Provide a name for this Color, e.g. <em>scarlet</em> or <em>forest green</em>.', max_length=200, unique=True)),
                ('h', models.PositiveIntegerField(default=0, help_text='Select a Hue from 0-255.')),
                ('s', models.DecimalField(decimal_places=2, default=0.0, help_text='Select a Saturation as a decimal percentage.', max_digits=3)),
                ('l', models.DecimalField(decimal_places=2, default=0.0, help_text='Select a Lightness/Brightness as a decimal percentage.', max_digits=3)),
                ('a', models.DecimalField(decimal_places=2, default=0.0, help_text='Select a Alpha/Transparency as a decimal percentage.', max_digits=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DateAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveIntegerField(default=0, help_text='Provide a display order.')),
                ('object_id', models.PositiveIntegerField(help_text='Provide the actual object ID of the generic relation within the table of the Content Type.')),
                ('source_accessed', models.DateField(blank=True, default=django.utils.timezone.now, help_text='When was this source consulted.')),
                ('category', models.CharField(choices=[('START', 'Birth'), ('END', 'Death')], default='START', help_text='What type of date is this?', max_length=50)),
                ('content_type', models.ForeignKey(help_text='Provide the model name for the generic relation.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'dates',
                'verbose_name': 'date',
            },
        ),
        migrations.CreateModel(
            name='DescriptionAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveIntegerField(default=0, help_text='Provide a display order.')),
                ('object_id', models.PositiveIntegerField(help_text='Provide the actual object ID of the generic relation within the table of the Content Type.')),
                ('source_accessed', models.DateField(blank=True, default=django.utils.timezone.now, help_text='When was this source consulted.')),
                ('body', models.TextField(help_text='Provide a date snippet from the original context.')),
                ('content_type', models.ForeignKey(help_text='Provide the model name for the generic relation.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'descriptions',
                'verbose_name': 'description',
            },
        ),
        migrations.CreateModel(
            name='EmailAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveIntegerField(default=0, help_text='Provide a display order.')),
                ('object_id', models.PositiveIntegerField(help_text='Provide the actual object ID of the generic relation within the table of the Content Type.')),
                ('source_accessed', models.DateField(blank=True, default=django.utils.timezone.now, help_text='When was this source consulted.')),
                ('category', models.CharField(choices=[('PRIMARY', 'primary'), ('SECONDARY', 'secondary'), ('WORK', 'work'), ('HOME', 'home'), ('INFODESK', 'main information desk')], default='PRIMARY', help_text='What type of email address is this?', max_length=50)),
                ('email', models.CharField(help_text='Provide an email address, e.g. <pre>allan@example.com</pre>.', max_length=200, unique=True)),
                ('content_type', models.ForeignKey(help_text='Provide the model name for the generic relation.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'emails',
                'verbose_name': 'email',
            },
        ),
        migrations.CreateModel(
            name='IdentifierAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveIntegerField(default=0, help_text='Provide a display order.')),
                ('object_id', models.PositiveIntegerField(help_text='Provide the actual object ID of the generic relation within the table of the Content Type.')),
                ('source_accessed', models.DateField(blank=True, default=django.utils.timezone.now, help_text='When was this source consulted.')),
                ('identifier', models.CharField(help_text='An identifier from the original context, like a DOI, LoC, or museum accession number.', max_length=200, unique=True)),
                ('content_type', models.ForeignKey(help_text='Provide the model name for the generic relation.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'identifiers',
                'verbose_name': 'identifier',
            },
        ),
        migrations.CreateModel(
            name='ImageAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveIntegerField(default=0, help_text='Provide a display order.')),
                ('object_id', models.PositiveIntegerField(help_text='Provide the actual object ID of the generic relation within the table of the Content Type.')),
                ('source_accessed', models.DateField(blank=True, default=django.utils.timezone.now, help_text='When was this source consulted.')),
                ('content_type', models.ForeignKey(help_text='Provide the model name for the generic relation.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'images',
                'verbose_name': 'image',
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('slug', models.SlugField(help_text='Work from the general to the specific, e.g. <em>last-name-first-name</em>.', max_length=200, unique=True)),
                ('name', models.CharField(help_text='Provide a name for this License, e.g. <em>MIT license</em> or <em>Gnu Public License v. 2</em>.', max_length=200, unique=True)),
                ('url', models.URLField(help_text='Provide a URL for the source of this License.', unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('slug', models.SlugField(help_text='Work from the general to the specific, e.g. <em>last-name-first-name</em>.', max_length=200, unique=True)),
                ('name', models.CharField(help_text='Provide the canonical name for this Organization.', max_length=200, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrgOrgRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('DEPARTMENT', 'is department of'), ('LOCATED', 'is located in'), ('MEMBER', 'is member of'), ('OWNED', 'is owned by'), ('PART', 'is part of')], default='DEPARTMENT', help_text='Select a qualifier for this relationship.', max_length=50)),
                ('child', models.ForeignKey(help_text='Select a child Organization.', on_delete=django.db.models.deletion.CASCADE, related_name='children', to='collection.Organization')),
                ('parent', models.ForeignKey(help_text='Select a parent Organization.', on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='collection.Organization')),
            ],
            options={
                'verbose_name': 'organization relationship',
            },
        ),
        migrations.CreateModel(
            name='OrgPersonRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('EMPLOYED', 'is employed by'), ('CREATOR', 'is creator of'), ('MEMBER', 'is member of')], default='EMPLOYED', help_text='Select a qualifier for this relationship.', max_length=50)),
                ('organization', models.ForeignKey(help_text='Select a parent Organization.', on_delete=django.db.models.deletion.CASCADE, related_name='organizations', to='collection.Organization')),
            ],
            options={
                'verbose_name': 'member',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('slug', models.SlugField(help_text='Work from the general to the specific, e.g. <em>last-name-first-name</em>.', max_length=200, unique=True)),
                ('name_last', models.CharField(help_text='Provide a surname.', max_length=200)),
                ('name_first', models.CharField(blank=True, help_text='Provide other names here, including given and middle names.', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
        migrations.CreateModel(
            name='PhoneAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveIntegerField(default=0, help_text='Provide a display order.')),
                ('object_id', models.PositiveIntegerField(help_text='Provide the actual object ID of the generic relation within the table of the Content Type.')),
                ('source_accessed', models.DateField(blank=True, default=django.utils.timezone.now, help_text='When was this source consulted.')),
                ('category', models.CharField(choices=[('PRIMARY', 'primary'), ('SECONDARY', 'secondary'), ('WORK', 'work'), ('HOME', 'home'), ('INFODESK', 'main information desk')], default='PRIMARY', help_text='What type of phone number is this?', max_length=50)),
                ('phone', models.CharField(help_text='Provide a phone number, e.g. <pre>(312) 987-6543</pre>', max_length=200, unique=True)),
                ('content_type', models.ForeignKey(help_text='Provide the model name for the generic relation.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'phones',
                'verbose_name': 'phone',
            },
        ),
        migrations.CreateModel(
            name='Photograph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('slug', models.SlugField(help_text='Work from the general to the specific, e.g. <em>last-name-first-name</em>.', max_length=200, unique=True)),
                ('title', models.CharField(help_text='Provide a title.', max_length=200, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlaceAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveIntegerField(default=0, help_text='Provide a display order.')),
                ('object_id', models.PositiveIntegerField(help_text='Provide the actual object ID of the generic relation within the table of the Content Type.')),
                ('source_accessed', models.DateField(blank=True, default=django.utils.timezone.now, help_text='When was this source consulted.')),
                ('latitude', models.DecimalField(decimal_places=7, help_text='Provide a latitude of the place centroid.', max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=7, help_text='Provide a longitude of the place centroid.', max_digits=10)),
                ('altitude', models.DecimalField(decimal_places=2, default=0.0, help_text='Provide an altitude, in meters above sea level.', max_digits=10)),
                ('radius', models.DecimalField(blank=True, decimal_places=2, help_text='Allows a simple approximate area for this point, in meters.', max_digits=10)),
                ('content_type', models.ForeignKey(help_text='Provide the model name for the generic relation.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'places',
                'verbose_name': 'place',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('content_type', models.CharField(choices=[('WEBSITE', 'website'), ('BOOK', 'book')], help_text='Select a Work model class referenced by this citation.', max_length=50)),
                ('book', models.ForeignKey(blank=True, help_text='Select if source is a book.', on_delete=django.db.models.deletion.CASCADE, to='collection.Book')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('slug', models.SlugField(help_text='Work from the general to the specific, e.g. <em>last-name-first-name</em>.', max_length=200, unique=True)),
                ('title', models.CharField(help_text='Provide a title.', max_length=200, unique=True)),
                ('license', models.ForeignKey(help_text='Select a license for this software tool.', on_delete=django.db.models.deletion.CASCADE, to='collection.License')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VersionAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveIntegerField(default=0, help_text='Provide a display order.')),
                ('object_id', models.PositiveIntegerField(help_text='Provide the actual object ID of the generic relation within the table of the Content Type.')),
                ('source_accessed', models.DateField(blank=True, default=django.utils.timezone.now, help_text='When was this source consulted.')),
                ('content_type', models.ForeignKey(help_text='Provide the model name for the generic relation.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('source', models.ForeignKey(blank=True, help_text='Provide a citation for this attribute.', null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.Source')),
            ],
            options={
                'verbose_name_plural': 'versions',
                'verbose_name': 'version',
            },
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('slug', models.SlugField(help_text='Work from the general to the specific, e.g. <em>last-name-first-name</em>.', max_length=200, unique=True)),
                ('title', models.CharField(help_text='Provide a title.', max_length=200, unique=True)),
                ('url', models.URLField(help_text='Provide the root URL for this Website, in the form <pre>http://example.com/</pre>.', unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='source',
            name='website',
            field=models.ForeignKey(blank=True, help_text='Select if source is a website.', on_delete=django.db.models.deletion.CASCADE, to='collection.Website'),
        ),
        migrations.AddField(
            model_name='placeattr',
            name='source',
            field=models.ForeignKey(blank=True, help_text='Provide a citation for this attribute.', null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.Source'),
        ),
        migrations.AddField(
            model_name='phoneattr',
            name='source',
            field=models.ForeignKey(blank=True, help_text='Provide a citation for this attribute.', null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.Source'),
        ),
        migrations.AddField(
            model_name='orgpersonrelationship',
            name='person',
            field=models.ForeignKey(help_text='Select a Person who is part of this Organization.', on_delete=django.db.models.deletion.CASCADE, related_name='people', to='collection.Person'),
        ),
        migrations.AddField(
            model_name='organization',
            name='related_organizations',
            field=models.ManyToManyField(help_text='Select or create a related Organization.', through='collection.OrgOrgRelationship', to='collection.Organization'),
        ),
        migrations.AddField(
            model_name='organization',
            name='related_people',
            field=models.ManyToManyField(help_text='Select or create a related (member) Person.', related_name='organizations', through='collection.OrgPersonRelationship', to='collection.Person'),
        ),
        migrations.AddField(
            model_name='imageattr',
            name='source',
            field=models.ForeignKey(blank=True, help_text='Provide a citation for this attribute.', null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.Source'),
        ),
        migrations.AddField(
            model_name='identifierattr',
            name='source',
            field=models.ForeignKey(blank=True, help_text='Provide a citation for this attribute.', null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.Source'),
        ),
        migrations.AddField(
            model_name='emailattr',
            name='source',
            field=models.ForeignKey(blank=True, help_text='Provide a citation for this attribute.', null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.Source'),
        ),
        migrations.AddField(
            model_name='descriptionattr',
            name='source',
            field=models.ForeignKey(blank=True, help_text='Provide a citation for this attribute.', null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.Source'),
        ),
        migrations.AddField(
            model_name='dateattr',
            name='source',
            field=models.ForeignKey(blank=True, help_text='Provide a citation for this attribute.', null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.Source'),
        ),
        migrations.AddField(
            model_name='altnameattr',
            name='source',
            field=models.ForeignKey(blank=True, help_text='Provide a citation for this attribute.', null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.Source'),
        ),
        migrations.AddField(
            model_name='addressattr',
            name='source',
            field=models.ForeignKey(blank=True, help_text='Provide a citation for this attribute.', null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.Source'),
        ),
    ]
