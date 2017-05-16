# -*- coding: utf-8 *-*
from django.conf.urls import url, include
from medgointranet.views import *
from django.contrib.auth.views import  password_reset_done, password_reset_complete

urlpatterns = [
      # Home
      # url(r'^$', general_views.HomeIntranet, name= "HomeIntranet"), 
]



