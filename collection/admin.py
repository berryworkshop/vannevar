from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from collection.models import (
    Entity,
    Organization,
    Person,
    DateAttr,
    DescriptionAttr,
    Work,
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

class OrgChildInline(admin.TabularInline):
    verbose_name='sub-organization'
    model = Organization.related_organizations.through
    extra = 0
    fk_name = 'child'

class OrgParentInline(admin.TabularInline):
    verbose_name='super-organization'
    model = Organization.related_organizations.through
    extra = 0
    fk_name = 'parent'

class OrgChildPersonInline(admin.TabularInline):
    model = Organization.related_people.through
    extra = 0

class PersonParentOrgInline(admin.TabularInline):
    model = Person.organizations.through
    extra = 0


#
# Admins
# # #


class OrganizationAdmin(admin.ModelAdmin):
    fields = ['name', 'slug']
    prepopulated_fields = {'slug': ['name']}
    inlines = [
        DateAttrInline,
        DescriptionAttrInline,
        OrgChildInline,
        OrgParentInline,
        OrgChildPersonInline,
    ]


class PersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name_last', 'name_first']}
    inlines = [
        DateAttrInline,
        DescriptionAttrInline,
        PersonParentOrgInline,
    ]

class WorkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    inlines = [
        DateAttrInline,
        DescriptionAttrInline,
    ]

#
# Registration
# # #

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Work, WorkAdmin)