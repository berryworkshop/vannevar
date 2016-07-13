from django.db import models
from django.utils.timezone import now


class Item(models.Model):
    class Meta:
        abstract=True

    dates = models.ManyToManyField('Date')


class Source(models.Model):
    description = models.TextField()
    url = models.URLField()
    accessed = models.DateField(default=now)


class Color(models.Model):
    name = models.CharField(max_length=50)
    hue = models.DecimalField(max_digits=6, decimal_places=3)
    saturation = models.DecimalField(max_digits=6, decimal_places=3)
    lightness = models.DecimalField(max_digits=6, decimal_places=3)
    alpha = models.DecimalField(max_digits=4, decimal_places=3)


#
# Attributes
# # #

class Attribute(models.Model):
    class Meta:
        abstract=True

    source = models.ForeignKey('Source', blank=True, null=True)


class Date(Attribute):
    # TODO: perhaps refactor with http://stackoverflow.com/a/849426/652626
    # at least year needs not be naïve (BCE), and validation unique together
    year = models.IntegerField(blank=False)
    month = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "{}-{}-{}".format(self.year, self.month, self.day)


class Name(Attribute):
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name


#
# Entities
# # #

class Entity(Item):
    class Meta:
        abstract=True


class Organization(Entity):
    name = models.ForeignKey('Name')


class Person(Entity):
    name_last  = models.CharField(max_length=200, blank=False, null=False)
    name_first = models.CharField(max_length=200, blank=True, null=True)


#
# Works
# # #

class Work(Item):
    class Meta:
        abstract=True


class Tool(Work):
    pass