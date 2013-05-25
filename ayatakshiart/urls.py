from django.conf.urls import patterns, include, url
import settings
import common.views
import bio.views
import faq.views
import contact.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ayatakshiart.views.home', name='home'),
    # url(r'^ayatakshiart/', include('ayatakshiart.foo.urls')),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^home/', common.views.home, name='home'),
    url(r'^bio/', bio.views.bio, name='bio'),
    url(r'^url/', bio.views.bio, name='url'),
    url(r'^faq/', faq.views.faq, name='faq'),
    url(r'^contact/', contact.views.contact, name='contact'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

