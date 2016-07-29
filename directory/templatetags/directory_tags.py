from django import template
from directory.models import OrganizationPage

register = template.Library()

# OrganizationPage snippets
# docs: http://docs.wagtail.io/en/v1.5.2/topics/snippets.html
# @register.simple_tag
# def orgs():
#     return OrganizationPage.objects.all()