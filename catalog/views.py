from django.views.generic import DetailView, ListView
from .models import Organization, OrgOrgRelationship


class OrganizationView(DetailView):
    template_name = "catalog/organization.html"
    model = Organization


class OrganizationsView(ListView):
    template_name = "catalog/organizations.html"
    model = Organization

    def get_context_data(self, **kwargs):
        context = super(OrganizationsView, self).get_context_data(**kwargs)

        # objects are organizations not departments of other organizations.
        context['object_list'] = Organization.objects.exclude(
            parent_relation_set__category='DEPARTMENT')

        return context