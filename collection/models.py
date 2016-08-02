from django.db import models
from django.utils.timezone import now
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.core.validators import MaxValueValidator

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
    events = GenericRelation('EventAttr',
        related_query_name="%(class)s",
        )

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
        return str(self.date)


#
# Entities
# # #


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
        )
    address = models.TextField(    
        help_text="Provide the canonical physical address for this Organization.",
        unique=True,
        blank=True,
        )

    related_organizations = models.ManyToManyField('Organization',
        through='OrgOrgRelationship',
        through_fields=('parent', 'child'),
        symmetrical=False,
        help_text="Select or create a related Organization.",
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