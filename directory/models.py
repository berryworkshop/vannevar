from django.db import models
from django.utils.timezone import now
from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
)
from wagtail.wagtailsearch import index
from vannevar.models import RelatedLink


# 
# Index Pages
# # #

class DirectoryIndexPage(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('related_links', label="Related links"),
    ]


class DirectoryIndexRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('DirectoryIndexPage', related_name='related_links')


#
# Attributes
# # #

class Attribute(models.Model):
    is_abstract = True
    class Meta:
        abstract = True

    CATEGORIES = (
        ('PRIMARY','primary'),
        ('SECONDARY','secondary'),
    )
    category = models.CharField(max_length=20, choices=CATEGORIES, blank=False, default="PRIMARY")
    panels = [
        FieldPanel('category'),
    ]


class RelatedDate(Attribute):
    is_abstract = True
    class Meta:
        abstract = True

    categories = (
        ('START','start date'),
        ('END','end date'),
    )
    Attribute._meta.get_field('category').choices = categories

    date = models.DateField(default=now)
    panels = Attribute.panels + [
        FieldPanel('date'),
    ]


class RelatedPhone(Attribute):
    is_abstract = True
    class Meta:
        abstract = True

    categories = (
        ('HOME','work phone'),
        ('WORK','home phone'),
    )
    Attribute._meta.get_field('category').choices = categories

    number = models.CharField(max_length=50)
    panels = Attribute.panels + [
        FieldPanel('number'),
    ]




# 
# Item Pages
# # #

class ItemPage(Page):
    is_abstract = True
    class Meta:
        abstract = True



class EntityPage(Page):
    is_abstract = True
    class Meta:
        abstract = True


class OrganizationPageRelatedDates(Orderable, RelatedDate):
    page = ParentalKey('directory.OrganizationPage', related_name='related_dates')

class OrganizationPageRelatedPhones(Orderable, RelatedPhone):
    page = ParentalKey('directory.OrganizationPage', related_name='related_phones')


class OrganizationPage(EntityPage):
    CATEGORIES = (
        ('LIBRARY','Library'),
        ('ARCHIVE','Archive'),
        ('MUSEUM','Museum'),
        ('SCHOOL','School'),
        ('COMPANY','Company'),
        ('CONSORTIUM','Consortium'),
    )
    SCOPES = (
        ("INACTIVE", "Inactive/Closed"),
        ("LOCAL", "Local"),
        ("REGIONAL", "Regional"),
        ("NATIONAL", "National"),
        ("INTERNATIONAL", "International"),
    )
    category = models.CharField(
        max_length=23,
        choices=CATEGORIES,
        default="LIBRARY",
    )
    for_profit = models.BooleanField(default=False)
    scope = models.CharField(
        max_length=23,
        choices=SCOPES,
        default="LOCAL",
    )
    content_panels = Page.content_panels + [
        FieldPanel('category'),
        FieldPanel('for_profit'),
        FieldPanel('scope'),
        InlinePanel('related_dates', label="Related Dates" ),
        InlinePanel('related_phones', label="Related Phones" ),

    ]


class PersonPageRelatedDates(Orderable, RelatedDate):
    page = ParentalKey('directory.PersonPage', related_name='related_dates')

class PersonPageRelatedPhones(Orderable, RelatedDate):
    page = ParentalKey('directory.PersonPage', related_name='related_phones')

class PersonPage(EntityPage):
    name_last = models.CharField(max_length=255, verbose_name="First Name")
    name_first = models.CharField(max_length=255, verbose_name="Last Name")

    content_panels = Page.content_panels + [
        FieldPanel('name_last'),
        FieldPanel('name_first'),
    ]


# class WorkPage(ItemPage):
#     is_abstract = True
#     class Meta:
#         abstract = True


#
# Misc. Tables
# # #

class Citation(models.Model):
    pass
