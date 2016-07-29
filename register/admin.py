from django.contrib import admin
from .models import Organization, Person, DateAttribute



class OrganizationAdmin(admin.ModelAdmin):
    filter_horizontal = ['dates']

class PersonAdmin(admin.ModelAdmin):
    pass


class DateAttributeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(DateAttribute, DateAttributeAdmin)