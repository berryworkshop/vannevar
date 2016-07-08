import datetime

from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import (FieldPanel,
                                                FieldRowPanel,
                                                InlinePanel)
from wagtail.wagtailsearch import index

from vannevar.models import RelatedLink


class DirectoryIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('related_links', label="Related links"),
    ]

    def get_context(self, request):
        # makes me nervous, but: http://stackoverflow.com/questions/32626815/wagtail-views-extra-context
        context = super(DirectoryIndexPage, self).get_context(request)
        context['organization_pages_all'] = OrganizationPage.objects.all()
        return context


class DirectoryIndexRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('DirectoryIndexPage', related_name='related_links')


class ItemPage(Page):
    is_abstract = True
    class Meta:
        abstract = True

    date = models.DateField(verbose_name="Post Date", default=datetime.date.today)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body', classname="full")
    ]


class EntityPage(ItemPage):
    is_abstract = True
    class Meta:
        abstract = True


class PersonPage(EntityPage):
    name_last = models.CharField(max_length=255, verbose_name="First Name")
    name_first = models.CharField(max_length=255, verbose_name="Last Name")

    content_panels = EntityPage.content_panels + [
        FieldPanel('name_last'),
        FieldPanel('name_first'),
    ]


class OrganizationPage(EntityPage):
    
    # org_categories = (
    #     ("LIBRARY", "Library"),
    #     ("ARCHIVE", "Archive"),
    #     ("MUSEUM", "Museum"),
    #     ("SCHOOL", "School"),
    #     ("COMPANY", "Company"),
    #     ("CONSORTIUM", "Consortium"),
    #     ("DEPARTMENT", "department / unit"),
    # )

    org_scopes = (
        ("INACTIVE", "Inactive/Closed"),
        ("LOCAL", "Local"),
        ("REGIONAL", "Regional"),
        ("NATIONAL", "National"),
        ("INTERNATIONAL", "International"),
    )

    # category = models.MultipleChoiceField(max_length=23, choices=org_categories, default="LIBRARY", blank=False)
    for_profit = models.BooleanField(default=False)
    scope = models.CharField(max_length=23, choices=org_scopes, default="LOCAL", blank=False)

    content_panels = EntityPage.content_panels + [
        # FieldPanel('category'),
        FieldPanel('for_profit'),
        FieldPanel('scope'),
    ]


class WorkPage(ItemPage):
    is_abstract = True
    class Meta:
        abstract = True
