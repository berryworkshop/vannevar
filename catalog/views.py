from django.http import HttpResponse
from django.core import serializers
from django.views.generic import DetailView, ListView
from .models import Organization, OrgOrgRelationship

class OrganizationView(DetailView):
    '''
    Front-facing view for a single Organization.
    '''
    template_name = "catalog/organization.html"
    model = Organization


class OrganizationsView(ListView):
    '''
    View for a list of Organizations.
    '''
    template_name = "catalog/organizations.html"
    model = Organization

    def get_queryset(self):
        '''
        Returned queryset should not include departments; just top-level orgs.
        '''
        return Organization.objects.exclude(
            parent_relation_set__category='DEPARTMENT')

    def get(self, request, *args, **kwargs):
        '''
        Override get to allow json response
        '''
        if request.GET.get('format') == 'json':
            data = serializers.serialize('json', self.get_queryset())
            return HttpResponse(data, content_type='application/json')
        else:
            return super().get(request, *args, **kwargs)

