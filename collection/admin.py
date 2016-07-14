from django.contrib import admin
from collection.models import Organization, Person, Tool, DateAttr, OrganizationNameAttr, PlaceAttr
from django.forms import Textarea, URLInput
from django.db import models

class OrganizationNameAttrInline(admin.TabularInline):
    model = OrganizationNameAttr
    fields = ['name', 'source', 'source_url', 'source_accessed']
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':40})},
        models.URLField: {'widget': URLInput(attrs={'rows':1, 'cols':40})},
    }


class OrganizationAdmin(admin.ModelAdmin):
    fields = ['dates']
    inlines = [OrganizationNameAttrInline]



admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Person)
admin.site.register(Tool)

admin.site.register(DateAttr)
admin.site.register(OrganizationNameAttr)
admin.site.register(PlaceAttr)
