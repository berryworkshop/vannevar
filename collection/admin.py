from django.contrib import admin
from django.db import models
from django.forms import Textarea, CheckboxSelectMultiple
from django.contrib.contenttypes.admin import GenericTabularInline
from collection.models import (
    OrganizationCategory,
    Organization,
    AltNameAttr,
    EventAttr,
    )

#
# Inlines
# # #

class EventAttrInline(GenericTabularInline):
    '''
    Provide for Organizations to have associated Events.
    '''
    verbose_name = 'event'
    verbose_name_plural = 'events'
    model = EventAttr
    extra = 0

class AltNameAttrInline(GenericTabularInline):
    '''
    Provide for Organizations to have Alternate Names.
    '''
    verbose_name = 'alternate name'
    verbose_name_plural = 'alternate names'
    model = AltNameAttr
    extra = 0

class OrgChildInline(admin.TabularInline):
    '''
    Provide for nested Organization children.
    '''
    verbose_name='sub-organization' 
    model = Organization.related_organizations.through
    extra = 0
    fk_name = 'parent'

class OrgParentInline(admin.TabularInline):
    '''
    Provide for nested Organization parents.
    '''
    verbose_name='super-organization'
    model = Organization.related_organizations.through
    extra = 0
    fk_name = 'child'


#
# Admins
# # #

class OrganizationAdmin(admin.ModelAdmin):
    '''
    Admin for Organization entry.
    '''
    fields = ['name', 'categories', 'tags', 'website', 'address', 'nonprofit', 'slug']
    list_display = ['name', 'categories_', 'tags_']
    prepopulated_fields = {'slug': ['name']}
    inlines = [
        EventAttrInline,
        AltNameAttrInline,
        OrgChildInline,
        OrgParentInline,
    ]
    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={
                'rows': 1,
                'cols': 40,
                'style': 'height: 3em;'})},
        models.ManyToManyField: {
            'widget': CheckboxSelectMultiple},
    }

    def get_queryset(self, request):
        '''
        Keep from performing too many requests.
        '''
        return super(OrganizationAdmin, self).get_queryset(request).prefetch_related('tags', 'categories')

    def categories_(self, obj):
        '''
        Format an object's categories into a string for list_display
        '''
        categories = ', '.join(i.get_category_display() for i in obj.categories.all())
        return '{}'.format(categories)
    categories_.short_description = 'Categories'

    def tags_(self, obj):
        '''
        Format an object's tags into a string for list_display
        '''
        tags = ', '.join(i for i in obj.tags.names())
        return '{}'.format(tags)
    tags_.short_description = 'Tags'

#
# Registration
# # #
admin.site.register(Organization, OrganizationAdmin)
