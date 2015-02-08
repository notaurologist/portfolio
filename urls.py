from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to
from django.conf import settings

from django.contrib import admin
from admin import admin_site

urlpatterns = patterns('',
    url(r'^$', redirect_to, {'url': '/portfolio'}, name='index'),
    url(r'^portfolio/', 'portfolio.views.index', name='portfolio'),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/portfolio/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
