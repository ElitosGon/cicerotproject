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

		