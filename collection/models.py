from django.db import models
from django.utils.timezone import now
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey


class Item(models.Model):
    class Meta:
        abstract=True

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    # fields for (receiving) generic relations
    dates = GenericRelation('DateAttr',
        related_query_name="%(class)s",
        )
    descriptions = GenericRelation('DescriptionAttr',
        related_query_name="%(class)s",
        )

    def __str__(self):
        return self.name


class Color(Item):
    hue = models.DecimalField(max_digits=6, decimal_places=3)
    saturation = models.DecimalField(max_digits=6, decimal_places=3)
    lightness = models.DecimalField(max_digits=6, decimal_places=3)
    alpha = models.DecimalField(max_digits=4, decimal_places=3)

    def __str__(self):
        return self.name


class Source(Item):
    url = models.URLField()


#
# Attributes
# # #

class Attribute(models.Model):
    class Meta:
        abstract=True

    # fields for citation
    source = models.ForeignKey('Source', blank=True)
    source_accessed = models.DateField(default=now)

    # fields for presentation
    sequence = models.PositiveIntegerField(default=0)

    # fields for generic relations
    content_type = models.ForeignKey(ContentType,
        on_delete = models.CASCADE,
        default = ContentType.objects.get(
            app_label="collection", model="organization").pk
        )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return 'sequence: {}'.format(self.sequence)


class DateAttr(Attribute):
    # TODO: perhaps refactor with http://stackoverflow.com/a/849426/652626
    # at least year needs not be naïve (BCE), and validation unique together
    year = models.IntegerField()
    month = models.IntegerField(null=True, blank=True)
    day = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "{}-{}-{}".format(self.year, self.month, self.day)


class DescriptionAttr(Attribute):
    body = models.TextField()

    def __str__(self):
        return "{}-{}-{}".format(self.year, self.month, self.day)


#
# Entities
# # #

class Entity(Item):
    class Meta:
        abstract=True
    pass


class Organization(Entity):
    pass


class Person(Entity):
    name_last  = models.CharField(max_length=200)
    name_first = models.CharField(max_length=200, blank=True)


#
# Works
# # #

class Work(Item):
    class Meta:
        abstract=True


class Tool(Work):
    pass