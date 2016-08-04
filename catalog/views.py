from django.views.generic import TemplateView
from .models import Organization

class OrganizationsView(TemplateView):
    template_name = "catalog/organizations.html"

    def organizations(self):
        return Organization.objects.all()