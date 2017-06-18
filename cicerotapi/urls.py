# -*- coding: utf-8 *-*
from django.conf.urls import url, include
from django.contrib.auth.views import  password_reset_done, password_reset_complete
from django.conf.urls import url, include, i18n
from django.contrib import admin, admindocs
from django.conf import settings
from django.views.static import serve
from rest_framework import routers
from cicerotapi import views
import oauth2_provider.views as oauth2_views
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet


router = routers.DefaultRouter()
router.register(r'Region',views.RegionViewSet)
router.register(r'Provincia',views.ProvinciaViewSet)
router.register(r'Comuna',views.ComunaViewSet)
router.register(r'TipoTag',views.TipoTagViewSet)
router.register(r'Tag',views.TagViewSet)
router.register(r'EstadoTour',views.EstadoTourViewSet)
router.register(r'TipoTour',views.TipoTourViewSet)
router.register(r'TipoGuia',views.TipoGuiaViewSet)
router.register(r'RegistroGuia',views.RegistroGuiaViewSet)
router.register(r'Guia',views.GuiaViewSet)
router.register(r'Tour',views.TourViewSet)	
router.register(r'Horario',views.HorarioViewSet)
router.register(r'Pais',views.PaisViewSet)
router.register(r'Turista',views.TuristaViewSet)
router.register(r'Actividad',views.ActividadViewSet)
router.register(r'Rol',views.RolViewSet)
router.register(r'TextoSelect',views.TextoSelectViewSet)
router.register(r'Evaluacion',views.EvaluacionViewSet)
router.register(r'TipoMultimedia',views.TipoMultimediaViewSet)	
router.register(r'Multimedia',views.MultimediaViewSet)
router.register(r'Staff',views.StaffViewSet)
router.register(r'Favorito',views.FavoritoViewSet)
router.register(r'Suscripción',views.SuscripcionViewSet)
router.register(r'Transaccion',views.TransaccionViewSet)
router.register(r'InstanciaTour',views.InstanciaTourViewSet)
router.register(r'Inscripcion',views.InscripcionViewSet)
router.register(r'TipoServicio',views.TipoServicioViewSet)
router.register(r'ServicioTour',views.ServicioTourViewSet)
router.register(r'Comentario',views.ComentarioViewSet)
router.register(r'FCMDevice',views.FCMDeviceViewSet)			
 

urlpatterns = [
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^devices?$', FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_fcm_device'),
    url(r'^',include(router.urls)), 
]







