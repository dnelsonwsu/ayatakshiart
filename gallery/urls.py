from django.conf.urls import patterns, url

from gallery import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<medium>[\w\ ]+)/(?P<category>\w+)/$', views.gallery, name='gallery')
)
