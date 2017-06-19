from django import forms
from cicerotwebapp import models
from django.contrib import auth
from django.contrib.auth.models import User

class MensajeContactoForm(forms.ModelForm):
	class Meta:
		model = models.MensajeContacto
		fields = ["nombre",
				  "email",
				  "asunto",
				  "mensaje"]

	def __init__(self, *a, **kw):
		super(MensajeContactoForm, self).__init__(*a, **kw)
		self.fields['texto'].required = True 
		self.fields['nombre'].required = True 
		self.fields['email'].required = True
		self.fields['tipo'].required = True