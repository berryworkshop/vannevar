from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Organization


class OrganizationAdmin(ModelAdmin):
    model = Organization
    menu_icon = 'date'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    list_display = ('name', 'related_organizations', 'related_people', 'slug',
        # 'dates',
        # 'descriptions'
        )
    list_filter = ('name',)
    search_fields = ('name',)

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(OrganizationAdmin)