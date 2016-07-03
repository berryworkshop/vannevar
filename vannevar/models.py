from django.db import models

from wagtail.wagtailcore.models import Page

from wagtail.wagtailadmin.edit_handlers import (FieldPanel,
                                                MultiFieldPanel,
                                                PageChooserPanel)

from wagtail.wagtailadmin.edit_handlers import FieldPanel


# These models are for general use across various subapps.

class LinkFields(models.Model):

    class Meta:
        abstract = True

    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
    ]


# Related links
class RelatedLink(LinkFields):

    class Meta:
        abstract = True

    title = models.CharField(max_length=255, help_text="Link title")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]
