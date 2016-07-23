from django.db import models
from django.utils.timezone import now
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey


#
# Main
# # #


class Base(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField('Created', auto_now_add=True)
    modified = models.DateTimeField('Modified', auto_now=True)

    def __str__(self):
        return '{} {}: {}' % (self.__class__.__name__, self.id, self.slug)

    def to_json(self, include_related=True):
        return {
            'id': self.id,
            'slug': self.slug,
            'created': self.created.isoformat(),
            'modified': self.modified.isoformat(),
            'class_name': self.__class__.__name__,
        }


class Item(Base):
    class Meta:
        abstract = True

    slug = models.SlugField(max_length=200)

    # fields for (receiving) generic relations
    dates = GenericRelation('DateAttr',
        related_query_name="%(class)s",
        )
    descriptions = GenericRelation('DescriptionAttr',
        related_query_name="%(class)s",
        )


#
# Attributes
# # #

class Attribute(models.Model):
    class Meta:
        abstract=True
        ordering = ['sequence', 'id']

    # fields for presentation
    sequence = models.PositiveIntegerField(default=0)

    # fields for generic relations
    content_type = models.ForeignKey(ContentType,
        on_delete = models.CASCADE,
        default = ContentType.objects.get(
            app_label="collection", model="organization").pk
        )
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    # fields for citation
    source = models.ForeignKey('Source', blank=True, null=True)
    source_accessed = models.DateField(default=now, blank=True)

    def __str__(self):
        return '{} #{}'.format(self.name, self.sequence)



class DateAttr(Attribute):
    class Meta:
        verbose_name = 'date'
        verbose_name_plural = 'dates'

    date = models.DateField(default=now)

    categories = (
        ('START', 'Start'),
        ('END', 'End'),
    )
    category = models.CharField(
        max_length=50,
        choices=categories,
        default="START"
    )

    def __str__(self):
        return str(self.date)


class DescriptionAttr(Attribute):
    class Meta:
        verbose_name = 'description'
        verbose_name_plural = 'descriptions'

    body = models.TextField()

    def __str__(self):
        return self.body[:50]

#
# Entities
# # #

class Entity(Item):
    class Meta:
        abstract = True

    # fields for (receiving) generic relations


class Organization(Entity):
    name = models.CharField(max_length=200)

    related_organizations = models.ManyToManyField('Organization',
        through='OrgOrgRelationship',
        through_fields=('parent', 'child'),
        symmetrical=False
    )
    
    related_people = models.ManyToManyField('Person',
        through='OrgPersonRelationship',
        through_fields=('organization', 'person'),
        symmetrical=False,
        related_name='organizations'
    )

    def __str__(self):
        return self.name


class OrgOrgRelationship(models.Model):
    class Meta:
        verbose_name='organization relationship'

    parent = models.ForeignKey('Organization',
        on_delete=models.CASCADE,
        related_name='parents'
    )
    child = models.ForeignKey('Organization',
        on_delete=models.CASCADE,
        related_name='children'
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
    )


class OrgPersonRelationship(models.Model):
    class Meta:
        verbose_name='member'

    organization = models.ForeignKey('Organization',
        on_delete=models.CASCADE,
        related_name='organizations'
    )
    person = models.ForeignKey('Person',
        on_delete=models.CASCADE,
        related_name='people'
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
    )


class Person(Entity):
    class Meta:
        verbose_name_plural = 'people'

    name_last  = models.CharField(max_length=200)
    name_first = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return '{}, {}'.format(self.name_last, self.name_first)





#
# Works
# # #

class Source(Base):
    content_types = (
        ('WEBSITE', 'website'),
        ('BOOK', 'book'),
    )
    content_type = models.CharField(choices=content_types, max_length=50)

    book = models.ForeignKey('Book', blank=True)
    website = models.ForeignKey('Website', blank=True)

    # TODO: needs validation to require at least one foreign key.

    def cast(self):
        return 'blork'


class Work(Item):
    class Meta:
        abstract = True

    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Book(Work):
    pass


class Website(Work):
    pass


