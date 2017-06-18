# -*- coding: utf-8 *-*
from django.conf.urls import url, include
from cicerotwebapp.views import general_views
from django.contrib.auth.views import  password_reset_done, password_reset_complete

urlpatterns = [
      # Home
      url(r'^$', general_views.Home, name= "home"), 

]


