from django.views.generic import DetailView, TemplateView
from .models import Organization, OrgOrgRelationship


class OrganizationView(DetailView):
    template_name = "catalog/organization.html"
    model = Organization


class OrganizationsView(TemplateView):
    template_name = "catalog/organizations.html"

    def organizations_top(self):
        '''
        All organizations which are not departments of other organizations.
        '''
        return Organization.objects.exclude(
            parent_relation_set__category='DEPARTMENT')
