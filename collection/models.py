from django.db import models
from django.utils.timezone import now
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.core.validators import MaxValueValidator

from .controlled_vocabularies import contact_categories, iso_3166_1_alpha_3
from taggit.managers import TaggableManager

#
# Main
# # #

class Base(models.Model):
    '''
    The most rudimentary stuff, for use in every custom model.
    '''
    class Meta:
        abstract = True

    created = models.DateTimeField('Created',
        auto_now_add=True,
        )
    modified = models.DateTimeField('Modified',
        auto_now=True,
        )


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
    events = GenericRelation('EventAttr',
        related_query_name="%(class)s",
        )

    def to_json(self, include_related=True):
        return {
            'id': self.id,
            'slug': self.slug,
            'created': self.created.isoformat(),
            'modified': self.modified.isoformat(),
            'class_name': self.__class__.__name__,
        }

    def __str__(self):
        return '{} {}: {}' % (self.__class__.__name__, self.id, self.slug)


#
# Attributes
# # #

class Attribute(Base):
    '''
    The base for attributes attached to Items.
    '''
    class Meta:
        abstract=True

    # fields for generic relations
    content_type = models.ForeignKey(ContentType,
        on_delete = models.CASCADE,
        help_text="Provide the model name for the generic relation.",
        )
    object_id = models.PositiveIntegerField(
        help_text="Provide the actual object ID of the generic relation within the table of the Content Type.",
        )
    content_object = GenericForeignKey('content_type', 'object_id')


class AltNameAttr(Attribute):
    '''
    For tracking alternative names for organizations, like abbreviations.
    '''
    class Meta:
        verbose_name = 'alternate name'
        verbose_name_plural = 'alternate names'
 
    name = models.CharField(
         max_length = 200,
         help_text="Select an alternate Name, e.g. the abbreviation 'OCLC'.",
         )
    categories = (
            ('ABBREVIATION', 'abbreviation'),
            ('NICKNAME', 'nickname'),
        )
    category = models.CharField(
        max_length=50,
        choices=categories,
        default="ABBREVIATION",
        help_text="In what category is this name?",
        )
 
    def __str__(self):
        return self.get_category_display()


#class DescriptionAttr(Attribute):
#    '''
#    For tracking descriptive elements.
#    '''
#    class Meta:
#        verbose_name = 'description'
#        verbose_name_plural = 'descriptions'
# 
#    description = models.TextField(
#        help_text="Describe the organization in narrative form.",
#        )
#    categories = (
#        ('MISSION', 'an official mission statement'),
#        ('HISTORY', 'an historical narrative'),
#        ('FORM', 'appearance, situation or physical context'),
#        ('FUNCTION', 'operational documentation'),
#        )
#    category = models.CharField(
#        max_length=50,
#        choices=categories,
#        default="MISSION",
#        help_text="What sort of descriptive information is this?",
#        )
# 
#    def __str__(self):
#        return str(self.description)


class EventAttr(Attribute):
   '''
   For tracking events like birth dates and death dates.
   '''
   class Meta:
       verbose_name = 'event'
       verbose_name_plural = 'events'

   # TODO: figure out custom date field
   year = models.PositiveIntegerField(
       help_text="During what year did the event happen?",
       validators=[MaxValueValidator(9999)]
       )
   categories = (
       ('INCORPORATION', 'incorporation'),
       ('TERMINATION', 'termination'),
       )
   category = models.CharField(
       max_length=50,
       choices=categories,
       default="INCORPORATION",
       help_text="What is this event?",
       )

   def __str__(self):
       return str(self.year)

#
# Entities
# # #


class OrganizationCategory(Base):
    '''
    A controlled vocabulary for Organization categories.
    '''
    categories = (
        ('ARCHIVE', 'archive'),
        ('CONSORTIUM', 'consortium'),
        ('CORPORATION', 'corporation'),
        ('LIBRARY', 'library'),
        ('MUSEUM', 'museum'),
        ('SCHOOL', 'school'),
        )
    category = models.CharField(
        max_length=50,
        choices=categories,
        default="LIBRARY",
        help_text="What type of organization?",
        unique=True
        )

    def __str__(self):
        return self.get_category_display()


class Organization(Item):
    '''
    Companies, Communities, Nonprofits, Consortia.
    '''
    name = models.CharField(
        max_length=200,
        help_text="Provide the canonical name for this Organization.",
        unique=True,
        )
    website = models.URLField(
        help_text="Provide the canonical website URL for this Organization.",
        unique=True,
        blank=True,
        null=True,
        )
    address = models.TextField(
        help_text="Provide the canonical physical address for this Organization.",
        unique=True,
        blank=True,
        null=True,
        )
    nonprofit = models.BooleanField(
        default=True,
        help_text="Select whether or not this organization is organized as a not-for-profit entity."
        )

    # scopes
    # hat tip http://www.b-list.org/weblog/2007/nov/02/handle-choices-right-way/
    SCOPE_CLOSED = 0
    SCOPE_LOCAL = 1
    SCOPE_REGIONAL = 2
    SCOPE_NATIONAL = 3
    SCOPE_INTERNATIONAL = 4
    SCOPES = (
        (SCOPE_CLOSED, 'closed'),
        (SCOPE_LOCAL, 'local'),
        (SCOPE_REGIONAL, 'regional'),
        (SCOPE_NATIONAL, 'national'),
        (SCOPE_INTERNATIONAL, 'international'),
        )
    scope = models.IntegerField(
        help_text="What is the level of influence, reach, or exposure of this Organization?",
        choices=SCOPES,
        default=SCOPE_LOCAL,
        )

    categories = models.ManyToManyField(
        'OrganizationCategory',
        blank=True,
        )
    tags = TaggableManager(
        blank=True
        )
    related_organizations = models.ManyToManyField('Organization',
        through='OrgOrgRelationship',
        through_fields=('parent', 'child'),
        symmetrical=False,
        help_text="Select or create a related Organization.",
        blank=True,
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