from __future__ import absolute_import
from django.contrib.auth.decorators import login_required
from cicerotwebapp import models
from django.shortcuts import render, redirect
from django.template import RequestContext
from cicerotwebapp.forms import general_forms
from django.contrib import messages
from django.db import transaction
from collections import namedtuple
from fcm_django.models import FCMDevice
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.models import User
from django.conf import settings
from templated_email import send_templated_mail, get_templated_mail

DEBUG 	= 10
INFO 	= 20
SUCCESS = 25
WARNING = 30
ERROR 	= 40
CRITICAL = 50

####### HOME #####################################
def Home(request):
	if request.method == 'GET':
		guias = models.Guia.objects.all().order_by('-updated_at')[:4]
		contexto = {
		 'guias' :guias,
		}
		return render(request,'home.html', contexto , RequestContext(request))
	else:
		return render(request,'404.html', None, RequestContext(request))


def AboutUs(request):
	if request.method == 'GET':
		return render(request,'about_us.html', None , RequestContext(request))
	else:
		return render(request,'404.html', None, RequestContext(request))

def FAQs(request):
	if request.method == 'GET':
		return render(request,'faqs.html', None , RequestContext(request))
	else:
		return render(request,'404.html', None, RequestContext(request))

def OurServices(request):
	if request.method == 'GET':
		return render(request,'servicios.html', None , RequestContext(request))
	else:
		return render(request,'404.html', None, RequestContext(request))


def ContactUs(request):
	if request.method == 'GET':
		return render(request,'contact_us.html', {'reply': True} , RequestContext(request))
	else:
		if request.method == 'POST':
			nombre = request.POST.get("nombre")
			email = request.POST.get("email")
			asunto = request.POST.get("asunto")
			mensaje = request.POST.get("mensaje")
			mensaje_contacto = models.MensajeContacto(nombre=nombre, email=email, asunto=asunto, mensaje=mensaje)
			mensaje_contacto.save(force_insert=True)
			messages.add_message(request, SUCCESS, "Mensaje enviado exitosamente", extra_tags='success')
			return render(request,'contact_us.html', {'reply': False} , RequestContext(request))
		else:
			return render(request,'404.html', None, RequestContext(request))

def GetAllGuias(request):
	if request.method == 'GET':

		guias_list = models.Guia.objects.all().order_by('-updated_at')
		search = request.GET.get("search")
		guias = None

		if search:
			guias = guias_list.filter(Q(tags__texto_tag__contains=search)
									 |Q(tipos_guia__nombre_tipo_guia__contains=search)
									 |Q(usuario__first_name__contains=search)
									 |Q(usuario__last_name__contains=search)).distinct()
		else:
			guias = guias_list


		contexto = {
			'guias' : guias,
			'multimedia': models.Multimedia.objects.all(),
		}

		return render(request,'guias.html', contexto , RequestContext(request))
	else:
		return render(request,'404.html', None, RequestContext(request))

def GetGuia(request, id):
	if request.method == 'GET':
		try:
			guia = models.Guia.objects.get(pk=id)
		except models.Guia.DoesNotExist:
			raise Http404
		
		contexto = {
			'guia' : guia,
		}

		return render(request,'guia.html', contexto , RequestContext(request))
	else:
		return render(request,'404.html', None, RequestContext(request))

def GetAllLugares(request):
	if request.method == 'GET':
		return render(request,'lugares.html', None , RequestContext(request))
	else:
		return render(request,'404.html', None, RequestContext(request))

def GetTour(request, id):
	if request.method == 'GET':
		try:
			tour = models.Tour.objects.get(pk=id)
		except models.Guia.DoesNotExist:
			raise Http404

		contexto = {
			'tour': tour,
			'guia': tour.guia,
		}

		return render(request,'tour.html', contexto , RequestContext(request))
	else:
		return render(request,'404.html', None, RequestContext(request))

def GetAllTours(request):
	if request.method == 'GET':

		turistas_list = models.Tour.objects.all().order_by('-updated_at')
		search = request.GET.get("search")
		tours = None

		if search:
			tours = turistas_list.filter(Q(nombre_tour__contains=search)
										|Q(descripcion_tour__contains=search)
										|Q(guia__usuario__first_name__contains=search)
										|Q(guia__usuario__last_name__contains=search)
										|Q(guia__tags__texto_tag__contains=search)).distinct()
		else:
			tours = turistas_list


		contexto = {
			'tours' : tours,
			'multimedia': models.Multimedia.objects.all(),
		}

		return render(request,'tours.html', contexto , RequestContext(request))
	else:
		return render(request,'404.html', None, RequestContext(request))