from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from collection.models import (
    Entity,
    Organization,
    Person,
    IdentifierAttr,
    AltNameAttr,
    DateAttr,
    DescriptionAttr,
    Source,
    )

#
# Inlines
# # #

class IdentifierAttrInline(GenericTabularInline):
    model = IdentifierAttr
    extra = 0
    fields = [
        'identifier', 'source', 'source_accessed',
    ]


class AltNameAttrInline(GenericTabularInline):
    model = AltNameAttr
    extra = 0
    fields = [
        'name', 'source', 'source_accessed',
    ]


class DateAttrInline(GenericTabularInline):
    verbose_name = 'date'
    verbose_name_plural = 'dates'
    model = DateAttr
    extra = 0
    fields = [
        'category', 'source', 'source_accessed',
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
    fk_name = 'parent'

class OrgParentInline(admin.TabularInline):
    verbose_name='super-organization'
    model = Organization.related_organizations.through
    extra = 0
    fk_name = 'child'

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
        IdentifierAttrInline,
        AltNameAttrInline,
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


#
# Registration
# # #

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Source)