from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings

from django.conf.urls.i18n import i18n_patterns

import pages.urls

urlpatterns = [
    url(r'^django/', include(admin.site.urls)),
    url(r'^', include(pages.urls)),
    url(r'^404/$', TemplateView.as_view(template_name='404.html'), name='404'),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    url(r'^', include(pages.urls)),
    url(r'^404/$', TemplateView.as_view(template_name='404.html'), name='404'),
)


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
