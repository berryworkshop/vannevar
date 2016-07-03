from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import (FieldPanel,
                                                InlinePanel)
from wagtail.wagtailsearch import index

from vannevar.models import RelatedLink


class DirectoryIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('related_links', label="Related links"),
    ]

class DirectoryIndexRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('DirectoryIndexPage', related_name='related_links')


class ItemPage(Page):

    is_abstract = True
    class Meta:
        abstract = True

    date = models.DateField("Post date")
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
    pass


class WorkPage(ItemPage):
    pass
