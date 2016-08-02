from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from collection.models import (
    Organization,
    EventAttr,
    )

#
# Inlines
# # #

class EventAttrInline(admin.TabularInline):
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
    fields = ['name', 'slug']
    prepopulated_fields = {'slug': ['name']}
    inlines = [
        EventAttrInline,
    ]

#
# Registration
# # #

admin.site.register(Organization, OrganizationAdmin)
