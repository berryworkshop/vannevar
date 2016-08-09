from django.conf.urls import url
from .views import OrganizationView, OrganizationsView

urlpatterns = [
    url(r'^organizations/(?P<slug>[\w-]+)$', OrganizationView.as_view(), name='organization'),
    url(r'^organizations/$', OrganizationsView.as_view(), name='organizations'),
]