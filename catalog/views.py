from django.views.generic import TemplateView
from .models import Organization, OrgOrgRelationship

class OrganizationsView(TemplateView):
    template_name = "catalog/organizations.html"

    def organizations(self):
        '''
        All organizations.
        '''
        return Organization.objects.all()


    def organizations_top(self):
        '''
        All organizations which are not departments of other organizations.
        '''
        return Organization.objects.all().exclude(
            parent_relation_set__category='DEPARTMENT')
