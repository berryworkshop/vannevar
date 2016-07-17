from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from collection.models import (
    Organization, Person, Tool, Source, DateAttr, DescriptionAttr,
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

class ItemAdmin(admin.ModelAdmin):
    inlines = [
        DateAttrInline,
        DescriptionAttrInline
        ]
    prepopulated_fields = {'slug': ['name']}


#
# Registration
# # #

admin.site.register(Organization, ItemAdmin)
admin.site.register(Person, ItemAdmin)
admin.site.register(Tool, ItemAdmin)
admin.site.register(Source, ItemAdmin)