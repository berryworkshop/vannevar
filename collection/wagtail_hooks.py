from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from .models import Organization, Person


class OrganizationAdmin(ModelAdmin):
    model = Organization
    menu_icon = 'date'
    menu_order = 200
    add_to_settings_menu = False
    list_display = ('name', 'slug', )
    # prepopulated_fields = {'slug': ['name']} # TODO: does not work yet
    search_fields = ('name',)
    # inlines = [
    #     IdentifierAttrInline,
    #     AltNameAttrInline,
    #     DateAttrInline,
    #     DescriptionAttrInline,
    #     OrgChildInline,
    #     OrgParentInline,
    #     OrgChildPersonInline,
    # ]


class PersonAdmin(ModelAdmin):
    model = Person
    menu_icon = 'date'
    menu_order = 200
    add_to_settings_menu = False
    list_display = ('name_last', 'name_first')
    search_fields = ('name_last', 'name_first')
    # prepopulated_fields = {'slug': ['name_last', 'name_first']} # TODO
    # inlines = [
    #     DateAttrInline,
    #     DescriptionAttrInline,
    #     PersonParentOrgInline,
    # ]


# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(OrganizationAdmin)
modeladmin_register(PersonAdmin)