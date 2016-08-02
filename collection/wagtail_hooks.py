from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from .models import Organization


class OrganizationAdmin(ModelAdmin):
    model = Organization
    menu_icon = 'date'
    menu_order = 200
    add_to_settings_menu = False
    list_display = ('name', 'slug', )
    # fields = ['name', 'categories', 'tags', 'website', 'address', 'nonprofit', 'slug']

    # prepopulated_fields = {'slug': ['name']} # TODO: does not work yet
    search_fields = ('name',)
    # inlines = [
    #     EventAttrInline,
    #     OrgChildInline,
    #     OrgParentInline,
    # ]


# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(OrganizationAdmin)