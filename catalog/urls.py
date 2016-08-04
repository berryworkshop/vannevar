from django.conf.urls import url
from .views import OrganizationsView

urlpatterns = [
    url(r'^organizations/$', OrganizationsView.as_view()),
]