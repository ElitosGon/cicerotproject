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
		return render(request,'home.html', None , RequestContext(request))
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
		return render(request,'guias.html', None , RequestContext(request))
	else:
		return render(request,'404.html', None, RequestContext(request))

def GetAllLugares(request):
	if request.method == 'GET':
		return render(request,'lugares.html', None , RequestContext(request))
	else:
		return render(request,'404.html', None, RequestContext(request))

def GetTour(request):
	if request.method == 'GET':
		return render(request,'tour.html', None , RequestContext(request))
	else:
		return render(request,'404.html', None, RequestContext(request))