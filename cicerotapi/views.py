from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from rest_framework import status
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from django.conf import settings
from django.core.urlresolvers import reverse

from django.http import Http404
from rest_framework import status

from cicerotwebapp import models

from django.contrib import auth
from cicerotapi import serializers as serial
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework import permissions, routers, serializers, viewsets
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from django.db.models import Q
from django.contrib.auth.views  import password_reset, password_reset_confirm

from fcm_django.models import FCMDevice
from django.http import Http404, HttpResponse

from django.core.mail import EmailMessage
from templated_email import send_templated_mail, get_templated_mail
from django.template.loader import render_to_string, get_template

from rest_framework.decorators import api_view, permission_classes


# Servicios publicos y genericos

class RegionViewSet(viewsets.ModelViewSet):
    queryset = models.Region.objects.all()
    serializer_class = serial.RegionSerializers
        

class ProvinciaViewSet(viewsets.ModelViewSet):
	queryset = models.Provincia.objects.all()
	serializer_class = serial.ProvinciaSerializers

class ComunaViewSet(viewsets.ModelViewSet):
	queryset = models.Comuna.objects.all()
	serializer_class = serial.ComunaSerializers

class TipoTagViewSet(viewsets.ModelViewSet):
	queryset = models.TipoTag.objects.all()
	serializer_class = serial.TipoTagSerializers

class TagViewSet(viewsets.ModelViewSet):
	queryset = models.Tag.objects.all()
	serializer_class = serial.TagSerializers

class EstadoTourViewSet(viewsets.ModelViewSet):
	queryset = models.EstadoTour.objects.all()
	serializer_class = serial.EstadoTourSerializers

class TipoTourViewSet(viewsets.ModelViewSet):
	queryset = models.TipoTour.objects.all()
	serializer_class = serial.TipoTourSerializers
	

class TipoGuiaViewSet(viewsets.ModelViewSet):
	queryset = models.TipoGuia.objects.all()
	serializer_class = serial.TipoGuiaSerializers
	
	
class RegistroGuiaViewSet(viewsets.ModelViewSet):
	queryset = models.RegistroGuia.objects.all()
	serializer_class = serial.RegistroGuiaSerializers
	
class GuiaViewSet(viewsets.ModelViewSet):
	queryset = models.Guia.objects.all()
	serializer_class = serial.GuiaSerializers

class TourViewSet(viewsets.ModelViewSet):
	queryset = models.Tour.objects.all()
	serializer_class = serial.TourSerializers
	
class HorarioViewSet(viewsets.ModelViewSet):
	queryset = models.Horario.objects.all()
	serializer_class = serial.HorarioSerializers
		
class PaisViewSet(viewsets.ModelViewSet):
	queryset = models.Pais.objects.all()
	serializer_class = serial.PaisSerializers

class TuristaViewSet(viewsets.ModelViewSet):
	queryset = models.Turista.objects.all()
	serializer_class = serial.TuristaSerializers
	
class ActividadViewSet(viewsets.ModelViewSet):
	queryset = models.Actividad.objects.all()
	serializer_class = serial.ActividadSerializers

class RolViewSet(viewsets.ModelViewSet):
	queryset = models.Rol.objects.all()
	serializer_class = serial.RolSerializers	

class TextoSelectViewSet(viewsets.ModelViewSet):
	queryset = models.TextoSelect.objects.all()
	serializer_class = serial.TextoSelectSerializers

class EvaluacionViewSet(viewsets.ModelViewSet):
	queryset = models.Evaluacion.objects.all()
	serializer_class = serial.EvaluacionSerializers	

class TipoMultimediaViewSet(viewsets.ModelViewSet):
	queryset = models.TipoMultimedia.objects.all()
	serializer_class = serial.TipoMultimediaSerializers

class MultimediaViewSet(viewsets.ModelViewSet):
	queryset = models.Multimedia.objects.all()
	serializer_class = serial.MultimediaSerializers

class StaffViewSet(viewsets.ModelViewSet):
	queryset = models.Staff.objects.all()
	serializer_class = serial.StaffSerializers

class FavoritoViewSet(viewsets.ModelViewSet):
	queryset = models.Favorito.objects.all()
	serializer_class = serial.FavoritoSerializers	

class SuscripcionViewSet(viewsets.ModelViewSet):
	queryset = models.Suscripcion.objects.all()
	serializer_class = serial.SuscripcionSerializers	

class TransaccionViewSet(viewsets.ModelViewSet):
	queryset = models.Transaccion.objects.all()
	serializer_class = serial.TransaccionSerializers

class InstanciaTourViewSet(viewsets.ModelViewSet):
	queryset = models.InstanciaTour.objects.all()
	serializer_class = serial.InstanciaTourSerializers	

class InscripcionViewSet(viewsets.ModelViewSet):
	queryset = models.Inscripcion.objects.all()
	serializer_class = serial.InscripcionSerializers
	
class TipoServicioViewSet(viewsets.ModelViewSet):
	queryset = models.TipoServicio.objects.all()
	serializer_class = serial.TipoServicioSerializers

class ServicioTourViewSet(viewsets.ModelViewSet):
	queryset = models.ServicioTour.objects.all()
	serializer_class = serial.ServicioTourSerializers
		
class ComentarioViewSet(viewsets.ModelViewSet):
	queryset = models.Comentario.objects.all()
	serializer_class = serial.ComentarioSerializers				

class FCMDeviceViewSet(viewsets.ModelViewSet):
    serializer_class = serial.FCMDeviceSerializers
    queryset = FCMDevice.objects.all()    



