from django.db import models
from django.utils.timezone import now


# # # # # #
# Mixins  #
# # # # # #

class CategoryMixin(models.Model):
    is_abstract=True,
    class Meta:
        abstract=True
    CATEGORIES = (
        ("PRIMARY", "primary"),
        ("SECONDARY", "secondary"),
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORIES,
        default="PRIMARY",
    )


# # # # # # #
# Entities  #
# # # # # # #


class Entity(Item):
    start_date = models.DateField('')


class Organization(CategoryMixin, Entity):
    name = models.CharField(max_length=255, blank=False)
    def __init__(self, *args, **kwargs):
        super(Organization, self).__init__(*args, **kwargs)

        CATEGORIES = (
            ('ARCHIVE', 'archive'),
            ('COMPANY', 'company'),
            ('CONSORTIUM', 'consortium'),
            ('LIBRARY', 'library'),
            ('MUSEUM', 'museum'),
            ('SCHOOL', 'school'),
        )

        # keep categories dry
        # https://djangosnippets.org/snippets/2569/
        category_field = self._meta.get_field('category')
        category_field.choices = CATEGORIES

    def __str__(self):
        return self.name


class Person(Entity):
    name_first = models.CharField(max_length=255)
    name_last = models.CharField(max_length=255, blank=False)


# # # # # # # #
# Attributes  #
# # # # # # # #

class Attribute(CategoryMixin, models.Model):
    is_abstract=True
    class Meta:
        abstract=True

    item = models.ForeignKey(
        'Item',
        on_delete=models.PROTECT,
    )


class DateAttribute(Attribute):
    date = models.DateField(
        blank=False,
        default=now,
    )

    def __str__(self):
        return str(self.date)