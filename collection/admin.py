from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from collection.models import (
    Organization, Person, Tool, DateAttr, DescriptionAttr,
    )

#
# Inlines
# # #

class DateAttrInline(GenericTabularInline):
    model = DateAttr
    extra = 0


class DescriptionAttrInline(GenericTabularInline):
    model = DescriptionAttr
    extra = 0


#
# Admins
# # #

class OrganizationAdmin(admin.ModelAdmin):
    inlines = [
        DateAttrInline, DescriptionAttrInline
    ]


class PersonAdmin(admin.ModelAdmin):
    inlines = [
        DateAttrInline, DescriptionAttrInline
    ]


#
# Registration
# # #

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Tool)