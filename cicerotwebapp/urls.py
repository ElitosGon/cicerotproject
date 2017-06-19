# -*- coding: utf-8 *-*
from django.conf.urls import url, include
from cicerotwebapp.views import general_views
from django.contrib.auth.views import  password_reset_done, password_reset_complete

urlpatterns = [
      # Home
      url(r'^$', general_views.Home, name= "home"), 
      url(r'^about_us/$', general_views.AboutUs, name="aboutUs"),
      url(r'^faqs/$', general_views.FAQs, name="faqs"),
      url(r'^servicios/$', general_views.OurServices, name="servicios"),
      url(r'^contact_us/$', general_views.ContactUs, name="contactUs"),


      # SERVICIOS
      url(r'^guias/$', general_views.GetAllGuias, name="GetAllGuias"),
      url(r'^guias/perfil/(?P<id>\d+)/$', general_views.GetGuia, name="GetGuia"),

      url(r'^tour/detalle/(?P<id>\d+)/$', general_views.GetTour, name="GetTour"),
      url(r'^tours/$', general_views.GetAllTours, name="GetAllTours"),

      url(r'^lugares/', general_views.GetAllLugares, name="GetAllLugares"),
      url(r'^toureg/', general_views.GetTour, name="GetTour"),

]


