from django.conf.urls import *

from gallery import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<medium>[\w\ ]+)/(?P<category>[\w\ ]+)/(?P<image_name>[\w\ ]+)/$', views.gallery, name='gallery'),
    url(r'^(?P<medium>[\w\ ]+)/(?P<category>[\w\ ]+)/$', views.gallery, name='gallery'),
    url(r'^(?P<medium>[\w\ ]+)/$', views.gallery, name='gallery')
)
