from django.db import models
from django.utils.timezone import now
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey

from .controlled_vocabularies import contact_categories, iso_3166_1_alpha_3


#
# Main
# # #


class Base(models.Model):
    '''
    The most rudimentary stuff, for use in every custom model.
    '''
    class Meta:
        abstract = True

    created = models.DateTimeField('Created', auto_now_add=True)
    modified = models.DateTimeField('Modified', auto_now=True)

    def __str__(self):
        return '{} {}' % (self.__class__.__name__, self.id)

    def to_json(self, include_related=True):
        return {
            'id': self.id,
            'slug': self.slug,
            'created': self.created.isoformat(),
            'modified': self.modified.isoformat(),
            'class_name': self.__class__.__name__,
        }


class Item(Base):
    '''
    The fundamental class connecting to attributes.
    '''
    class Meta:
        abstract = True

    slug = models.SlugField(max_length=200,
        help_text="Work from the general to the specific, e.g. <em>last-name-first-name</em>.",
        unique=True,
    )

    # fields for (receiving) generic relations
    dates = GenericRelation('DateAttr',
        related_query_name="%(class)s",
        help_text="Provide birth or death dates, for example."
        )
    descriptions = GenericRelation('DescriptionAttr',
        related_query_name="%(class)s",
        help_text="Provide from narrative sources."
        )

    def __str__(self):
        return '{} {}: {}' % (self.__class__.__name__, self.id, self.slug)

#
# Miscellaneous
# # #

class Source(Base):
    '''
    For Citations.
    '''
    content_types = (
        ('WEBSITE', 'website'),
        ('BOOK', 'book'),
    )
    content_type = models.CharField(choices=content_types,
        max_length=50,
        help_text="Select a Work model class referenced by this citation."
    )

    # TODO: refactor to use ContentType framework

    book = models.ForeignKey('Book',
        blank=True,
        help_text="Select if source is a book.",
    )
    website = models.ForeignKey('Website',
        blank=True,
        help_text="Select if source is a website.",
    )

    # TODO: needs validation to require at least one foreign key.

    def cast(self):
        return 'blork'


class License(Item):
    '''
    For software and other custom copyrights.
    '''
    name = models.CharField(
        max_length=200,
        help_text="Provide a name for this License, e.g. <em>MIT license</em> or <em>Gnu Public License v. 2</em>.",
        unique=True,
        )
    url = models.URLField(
        help_text="Provide a URL for the source of this License.",
        unique=True,
        )

    def __str__(self):
        return 'name'


class Color(Item):
    '''
    A simple class for storing colors.
    '''
    name = models.CharField(
        max_length=200,
        help_text="Provide a name for this Color, e.g. <em>scarlet</em> or <em>forest green</em>.",
        unique=True,
        )
    h = models.PositiveIntegerField(
        help_text="Select a Hue from 0-255.",
        default=0,
    )
    s = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        help_text="Select a Saturation as a decimal percentage.",
        default=0.00,
    )
    l = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        help_text="Select a Lightness/Brightness as a decimal percentage.",
        default=0.00,
    )
    a = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        help_text="Select a Alpha/Transparency as a decimal percentage.",
        default=0.00,
    )

    # TODO: validate maximum levels; validate decimals >= 0

#
# Attributes
# # #

class Attribute(models.Model):
    '''
    The base for attached attributes to Items.
    '''
    class Meta:
        abstract=True
        ordering = ['sequence', 'id']

    # fields for presentation
    sequence = models.PositiveIntegerField(
        default=0,
        help_text="Provide a display order.",
        )

    # fields for generic relations
    content_type = models.ForeignKey(ContentType,
        on_delete = models.CASCADE,
        help_text="Provide the model name for the generic relation.",
        )
    object_id = models.PositiveIntegerField(
        help_text="Provide the actual object ID of the generic relation within the table of the Content Type.",
        )
    content_object = GenericForeignKey('content_type', 'object_id')

    # fields for citation
    source = models.ForeignKey('Source',
        blank=True,
        null=True,
        help_text="Provide a citation for this attribute.",
        )
    source_accessed = models.DateField(
        default=now,
        blank=True,
        help_text="When was this source consulted.",
        )

    def __str__(self):
        return '{} #{}'.format(self.name, self.sequence)


class IdentifierAttr(Attribute):
    '''
    Custom Item IDs, like OID and external domain identification.
    '''
    class Meta:
        verbose_name = 'identifier'
        verbose_name_plural = 'identifiers'

    identifier = models.CharField(
        max_length=200,
        help_text="An identifier from the original context, like a DOI, LoC, or museum accession number.",
        unique=True,
        )

    def __str__(self):
        return self.identifier


class AltNameAttr(Attribute):
    '''
    Alternate names, abbreviations, and colloquialisms.
    '''
    class Meta:
        verbose_name = 'name'
        verbose_name_plural = 'names'

    name = models.CharField(
        max_length=200,
        help_text="What other names was the item known by?",
        unique=True,
        )

    def __str__(self):
        return self.name


class DateAttr(Attribute):
    '''
    For tracking birth dates, death dates, and other important date attributes.
    '''
    class Meta:
        verbose_name = 'date'
        verbose_name_plural = 'dates'

    # TODO: figure out custom date field
    # date = models.DateField(default=now)

    categories = (
        ('START', 'Birth'),
        ('END', 'Death'),
    )
    # TODO: figure out how to alter categories based on related content type.
    category = models.CharField(
        max_length=50,
        choices=categories,
        default="START",
        help_text="What type of date is this?",
    )

    def __str__(self):
        return str(self.date)


class DescriptionAttr(Attribute):
    '''
    Descriptions manually crafted or taken from primary sources.
    '''
    class Meta:
        verbose_name = 'description'
        verbose_name_plural = 'descriptions'

    body = models.TextField(
        help_text="Provide a date snippet from the original context.",
        )

    def __str__(self):
        return self.body[:50]


class PlaceAttr(Attribute):
    '''
    Basic geographic point data.
    '''
    class Meta:
        verbose_name = 'place'
        verbose_name_plural = 'places'

    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        help_text="Provide a latitude of the place centroid.",
        )
    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        help_text="Provide a longitude of the place centroid.",
        )
    altitude = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Provide an altitude, in meters above sea level.",
        default=0.0,
        )
    radius = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Allows a simple approximate area for this point, in meters.",
        blank=True,
        )

    # TODO: validate uniqueness


class ImageAttr(Attribute):
    '''
    Images.
    '''
    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'

    # TODO after relationship with Wagtail ironed out.

    pass


class VersionAttr(Attribute):
    '''
    Versions or editions for software and other media.
    '''
    class Meta:
        verbose_name = 'version'
        verbose_name_plural = 'versions'

    # TODO figure out version number field.
    # version = models.CharField(max_length=200)

    pass


class PhoneAttr(Attribute):
    '''
    Phone numbers.
    '''
    class Meta:
        verbose_name = 'phone'
        verbose_name_plural = 'phones'

    category = models.CharField(
        max_length=50,
        choices=contact_categories,
        help_text="What type of phone number is this?",
        default="PRIMARY",
        )

    phone = models.CharField(
        max_length=200,
        help_text="Provide a phone number, e.g. <pre>(312) 987-6543</pre>",
        unique=True,
        )
    # TODO validate phone number format


class EmailAttr(Attribute):
    '''
    Email addresses.
    '''
    class Meta:
        verbose_name = 'email'
        verbose_name_plural = 'emails'

    category = models.CharField(
        max_length=50,
        choices=contact_categories,
        help_text="What type of email address is this?",
        default="PRIMARY",
        )

    email = models.CharField(
        max_length=200,
        help_text = "Provide an email address, e.g. <pre>allan@example.com</pre>.",
        unique=True,
        )


class AddressAttr(Attribute):
    '''
    Postal addresses.
    '''
    class Meta:
        verbose_name = 'phone'
        verbose_name_plural = 'phones'

    category = models.CharField(
        max_length=50,
        choices=contact_categories,
        help_text="What type of postal address is this?",
        default="PRIMARY",
        )

    street = models.TextField(
        help_text="Provide a street address.  For a new line, press <pre>shift-enter</pre> (<pre>shift-return</pre> on a Mac).",
        )
    city = models.CharField(
        max_length=100,
        help_text="Provide a city or community name.",
        )
    state_region = models.CharField(max_length=100,
        help_text="Provide a state, province, or other region for postal purposes.",
        )
    postal_code = models.CharField(max_length=100,
        help_text="Provide a zip or other postal code.",
        )
    country = models.CharField(
        max_length=3,
        help_text="Select a nation or country.",
        choices=iso_3166_1_alpha_3,
        default='USA'
        )

    # TODO validate uniqueness somehow?


#
# Entities
# # #

class Entity(Item):
    '''
    Abstract shared characteristics between Organization and Person, because,
    you know, corporations are people too.
    TODO: delete?
    '''
    class Meta:
        abstract = True

    # fields for (receiving) generic relations


class Organization(Entity):
    '''
    Companies, Communities, Nonprofits, Consortia.
    '''
    name = models.CharField(
        max_length=200,
        help_text="Provide the canonical name for this Organization.",
        unique=True,
        )

    related_organizations = models.ManyToManyField('Organization',
        through='OrgOrgRelationship',
        through_fields=('parent', 'child'),
        symmetrical=False,
        help_text="Select or create a related Organization.",
    )
    
    related_people = models.ManyToManyField('Person',
        through='OrgPersonRelationship',
        through_fields=('organization', 'person'),
        symmetrical=False,
        related_name='organizations',
        help_text="Select or create a related (member) Person.",
    )

    def __str__(self):
        return self.name


class OrgOrgRelationship(models.Model):
    '''
    Construction for an organization web.
    '''
    class Meta:
        verbose_name='organization relationship'

    parent = models.ForeignKey('Organization',
        on_delete=models.CASCADE,
        related_name='parents',
        help_text="Select a parent Organization.",
    )
    child = models.ForeignKey('Organization',
        on_delete=models.CASCADE,
        related_name='children',
        help_text="Select a child Organization.",
    )
    categories = (
        ('DEPARTMENT', 'is department of'), 
        ('LOCATED', 'is located in'), 
        ('MEMBER', 'is member of'), 
        ('OWNED', 'is owned by'), 
        ('PART', 'is part of'), 
    )
    category = models.CharField(
        max_length=50,
        choices=categories,
        default='DEPARTMENT',   
        help_text="Select a qualifier for this relationship.",
    )

    # TODO: validate combination of parent and child?


class OrgPersonRelationship(models.Model):
    '''
    Allows People to be part of Organizations.
    '''
    class Meta:
        verbose_name='member'

    organization = models.ForeignKey('Organization',
        on_delete=models.CASCADE,
        related_name='organizations',
        help_text="Select a parent Organization.",
    )
    person = models.ForeignKey('Person',
        on_delete=models.CASCADE,
        related_name='people',
        help_text="Select a Person who is part of this Organization.",
    )
    categories = (
        ('EMPLOYED', 'is employed by'), 
        ('CREATOR', 'is creator of'), 
        ('MEMBER', 'is member of'), 
    )
    category = models.CharField(
        max_length=50,
        choices=categories,
        default='EMPLOYED',
        help_text="Select a qualifier for this relationship.",
    )

    # TODO: validate combination of org and person?


class Person(Entity):
    '''
    A dude or dudette.
    '''
    class Meta:
        verbose_name_plural = 'people'

    name_last  = models.CharField(
        max_length=200,
        help_text="Provide a surname.",
        )
    name_first = models.CharField(
        max_length=200,
        blank=True,
        help_text="Provide other names here, including given and middle names.",)

        # TODO validate uniqueness of Name Last and Name First

    def __str__(self):
        return '{}, {}'.format(self.name_last, self.name_first)





#
# Works
# # #


class Work(Item):
    '''
    A created artifact, digital or analog, real or imagined.
    '''
    class Meta:
        abstract = True

    title = models.CharField(
        max_length=200,
        help_text="Provide a title.",
        unique=True,
        )

    def __str__(self):
        return self.title


class Book(Work):
    '''
    Your basic codex form.
    '''
    pass


class Website(Work):
    '''
    Software or documents accessible via the Web.
    '''
    url = models.URLField(
        help_text="Provide the root URL for this Website, in the form <pre>http://example.com/</pre>.",
        unique=True,
        )


class Tool(Work):
    '''
    Software used by LAMs.
    '''
    license = models.ForeignKey('License',
        help_text="Select a license for this software tool.",
    )


class Photograph(Work):
    '''
    Distinct from Image, a Photograph is a representation of a physical object
    in a LAM's collection.
    '''
    pass


