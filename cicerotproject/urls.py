"""cicerotproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, i18n
from django.contrib import admin, admindocs
from django.conf import settings
from django.views.static import serve
from rest_framework import routers
from cicerotapi import urls

admin.autodiscover()

urlpatterns = [
    
    # Admin views
    url(r'^admin/', admin.site.urls),
    # CiceroT web views
    url(r'^', include('cicerotwebapp.urls', namespace='cicerotwebapp')),

    # Other views
    url(r'^i18n/', include(i18n)),
    url(r'^media/(?P<path>.*)$', serve , { 'document_root': settings.MEDIA_ROOT }),
    url(r'^static/(?P<path>.*)$', serve , { 'document_root':settings.STATIC_ROOT }),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # API URLS
    url(r'^api/', include('cicerotapi.urls', namespace='api')),
]

