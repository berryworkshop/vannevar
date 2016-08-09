from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User

from catalog import urls as catalog_urls
from cms import urls as cms_urls

urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),
    url(r'^catalog/', include(catalog_urls, namespace='catalog')),
    url(r'^', include(cms_urls, namespace='cms')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.views.generic import TemplateView

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
