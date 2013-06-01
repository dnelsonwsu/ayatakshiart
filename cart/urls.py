from django.conf.urls.defaults import *

import views

urlpatterns = patterns('',
    url(r'add/$', views.add_item_to_cart, name='addtocartajax'),
    url(r'remove/$', views.remove_item_from_cart, name='removefromcartajax'),
    url(r'view/$', views.view_cart, name='viewcart'),
)
