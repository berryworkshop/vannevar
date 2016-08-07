from django.db import models
from django.utils.timezone import now
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.core.validators import MaxValueValidator
from django.core.urlresolvers import reverse


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
        help_text="Work from the general to the specific, e.g. <em>last-name-first-name</em>.  If this is a generic name, affix with a parent acronym, e.g. <em>aic-prints-drawings</em>.",
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
    CATEGORIES = (
            ('ABBREVIATION', 'abbreviation'),
            ('NICKNAME', 'nickname'),
        )
    category = models.CharField(
        max_length=50,
        choices=CATEGORIES,
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
#    CATEGORIES = (
#        ('MISSION', 'an official mission statement'),
#        ('HISTORY', 'an historical narrative'),
#        ('FORM', 'appearance, situation or physical context'),
#        ('FUNCTION', 'operational documentation'),
#        )
#    category = models.CharField(
#        max_length=50,
#        choices=CATEGORIES,
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
   CATEGORIES = (
       ('INCORPORATION', 'incorporation'),
       ('TERMINATION', 'termination'),
       )
   category = models.CharField(
       max_length=50,
       choices=CATEGORIES,
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
    CATEGORIES = (
        ('ARCHIVE', 'archive'),
        ('ASSOCIATION', 'center'),
        ('CONSORTIUM', 'consortium'),
        ('CORPORATION', 'corporation'),
        ('FOUNDATION', 'foundation'),
        ('GALLERY', 'gallery'),
        ('LIBRARY', 'library'),
        ('MUSEUM', 'museum'),
        ('SCHOOL', 'school'),
        )

    category = models.CharField(
        max_length=50,
        choices=CATEGORIES,
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
    intro = models.CharField(
        max_length=250,
        help_text="Provide a short, precise, summary of this Organization.",
        blank=True,
        )
    website = models.URLField(
        help_text="Provide the canonical website URL for this Organization.",
        blank=True,
        )
    address = models.TextField(
        help_text="Provide the canonical physical address for this Organization.",
        blank=True,
        )
    nonprofit = models.BooleanField(
        default=True,
        help_text="Select whether or not this organization is organized as a not-for-profit entity."
        )

    # scopes
    # hat tip http://www.b-list.org/weblog/2007/nov/02/handle-choices-right-way/
    INACTIVE_SCOPE = 0
    MINOR_SCOPE = 1
    MODERATE_SCOPE = 2
    MAJOR_SCOPE = 3
    SUPER_SCOPE = 4
    SCOPES = (
        (INACTIVE_SCOPE, 'closed'),
        (MINOR_SCOPE, 'local'),
        (MODERATE_SCOPE, 'regional'),
        (MAJOR_SCOPE, 'national'),
        (SUPER_SCOPE, 'international'),
        )
    scope = models.IntegerField(
        help_text="What is the level of influence, reach, or exposure of this Organization within its industry?  This is a subjective rubric intended to imply scale or importance: an individual gallery, a supermarket, or a high school would be 'local'; a holding company, a city arts center, or a college would be 'regional'; most large corporations, museums, or state universities would be 'national'.  Only the largest, most famous entities, e.g. Microsoft, the Louvre, the New York Philharmonic, or Harvard University, are considered 'international'.",
        choices=SCOPES,
        default=MODERATE_SCOPE,
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

    def get_absolute_url(self):
        return reverse('catalog:organization', args=[self.slug])

    def child_organizations(self):
        '''All child Organizations.'''
        return Organization.objects.filter(parent_relation_set__parent=self)

    def parent_organizations(self):
        '''All parent Organizations.'''
        return Organization.objects.filter(child_relation_set__parent=self)


class OrgOrgRelationship(models.Model):
    '''
    Rels. for an organization web.
    '''
    class Meta:
        verbose_name='organization relationship'

    parent = models.ForeignKey('Organization',
        on_delete=models.CASCADE,
        related_name='child_relation_set', # from related parent
        help_text="Select a parent Organization.",
        )
    child = models.ForeignKey('Organization',
        on_delete=models.CASCADE,
        related_name='parent_relation_set', # from related child
        help_text="Select a child Organization.",
        )
    CATEGORIES = (
        ('DEPARTMENT', 'is department of'), 
        ('LOCATED', 'is located in'), 
        ('MEMBER', 'is member of'), 
        ('OWNED', 'is owned by'), 
        ('PART', 'is part of'), 
        )
    category = models.CharField(
        max_length=50,
        choices=CATEGORIES,
        default='DEPARTMENT',   
        help_text="Select a qualifier for this relationship.",
        )

    # TODO: validate combination of parent and child?