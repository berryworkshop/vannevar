from django.contrib import admin
from collection.models import Organization, Person, Tool, Date, Name, Source


admin.site.register(Organization)
admin.site.register(Person)
admin.site.register(Tool)
admin.site.register(Date)
admin.site.register(Name)
admin.site.register(Source)