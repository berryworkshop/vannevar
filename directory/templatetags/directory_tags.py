from django import template
from directory.models import *

register = template.Library()

# OrganizationPage snippets
# docs: http://docs.wagtail.io/en/v1.5.2/topics/snippets.html
@register.inclusion_tag('directory/directory_index_page.html', takes_context=True)
def organizations(context):
    return {
        'organizations': OrganizationPage.objects.all(),
        'request': context['request'],
    }