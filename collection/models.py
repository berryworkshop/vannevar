from django.db import models
from django.utils.timezone import now


class Item(models.Model):
    class Meta:
        abstract=True

    dates = models.ManyToManyField('DateAttr', blank=True)


class Color(models.Model):
    name = models.CharField(max_length=50)
    hue = models.DecimalField(max_digits=6, decimal_places=3)
    saturation = models.DecimalField(max_digits=6, decimal_places=3)
    lightness = models.DecimalField(max_digits=6, decimal_places=3)
    alpha = models.DecimalField(max_digits=4, decimal_places=3)


#
# Mixins
# # #

class SourceMixin(models.Model):
    class Meta:
        abstract=True

    source = models.TextField(blank=True)
    source_url = models.URLField(blank=True)
    source_accessed = models.DateField(default=now)


#
# Attributes
# # #

class Attribute(SourceMixin, models.Model):
    class Meta:
        abstract=True


class OrganizationNameAttr(Attribute):
    name = models.CharField(max_length=200)
    organization = models.ForeignKey('Organization', related_name="names")

    def __str__(self):
        return self.name


class DateAttr(Attribute):
    # TODO: perhaps refactor with http://stackoverflow.com/a/849426/652626
    # at least year needs not be naïve (BCE), and validation unique together
    year = models.IntegerField()
    month = models.IntegerField(null=True, blank=True)
    day = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "{}-{}-{}".format(self.year, self.month, self.day)


class PlaceAttr(Attribute):
    longitude = models.DecimalField(max_digits=6, decimal_places=3)
    latitude = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return "{}-{}-{}".format(self.longitude, self.latitude)



#
# Entities
# # #

class Entity(Item):
    class Meta:
        abstract=True


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