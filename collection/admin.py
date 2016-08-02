from django.contrib import admin
from django.db import models
from django.forms import Textarea
from django.contrib.contenttypes.admin import GenericTabularInline
from collection.models import (
    Organization,
    EventAttr,
    )

#
# Inlines
# # #

class EventAttrInline(GenericTabularInline):
    verbose_name = 'event'
    verbose_name_plural = 'events'
    model = EventAttr
    extra = 0

class OrgChildInline(admin.TabularInline):
    verbose_name='sub-organization'
    model = Organization.related_organizations.through
    extra = 0
    fk_name = 'parent'

class OrgParentInline(admin.TabularInline):
    verbose_name='super-organization'
    model = Organization.related_organizations.through
    extra = 0
    fk_name = 'child'

#
# Admins
# # #


class OrganizationAdmin(admin.ModelAdmin):
    fields = ['name', 'website', 'address', 'slug']
    prepopulated_fields = {'slug': ['name']}
    inlines = [
        EventAttrInline,
        OrgChildInline,
        OrgParentInline,
    ]
    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={
                'rows': 1,
                'cols': 40,
                'style': 'height: 3em;'})},
    }

#
# Registration
# # #

admin.site.register(Organization, OrganizationAdmin)
