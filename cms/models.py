from django.db import models
from django.utils.timezone import now

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from vannevar.models import RelatedLink


class HomePage(Page):
    pass


class ArticleIndexPage(Page):
    pass


class ArticlePage(Page):
    '''
    Generic article for website content.
    '''
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    date = models.DateField(
        "Post date",
        default=now,
        )
    intro = models.TextField(
        max_length=250,
        help_text="Provide a short, precise, summary of this Article.",
        blank=True,
        )
    body = RichTextField(
        blank=True
        )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        ImageChooserPanel('main_image'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full")
    ]