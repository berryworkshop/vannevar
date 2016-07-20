from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from collection.models import (
    Organization, Person, DateAttr, DescriptionAttr, Work
    )

#
# Inlines
# # #

class DateAttrInline(GenericTabularInline):
    verbose_name = 'date'
    verbose_name_plural = 'dates'
    model = DateAttr
    extra = 0
    fields = [
        'category', 'date', 'source', 'source_accessed',
    ]


class DescriptionAttrInline(GenericTabularInline):
    model = DescriptionAttr
    extra = 0
    fields = [
        'body', 'source', 'source_accessed',
    ]


#
# Admins
# # #

class StandardInlineMixin(admin.ModelAdmin):
    inlines = [
        DateAttrInline,
        DescriptionAttrInline
    ]

class OrganizationAdmin(StandardInlineMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


class PersonAdmin(StandardInlineMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name_last', 'name_first']}


class WorkAdmin(StandardInlineMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}


#
# Registration
# # #

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Work, WorkAdmin)