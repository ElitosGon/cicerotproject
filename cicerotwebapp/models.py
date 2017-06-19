#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-

# Librerias.
import os, sys
from django.db import models
from django.contrib import auth
from django_resized import ResizedImageField
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Q

class Region(models.Model):
	# SIMPLE FLIELD
	nombre_region = models.CharField(max_length=100, verbose_name="Nombre")
	sigla_region = models.CharField(max_length=100, verbose_name="Sigla")

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s Región %s" % (self.sigla_region, self.nombre_region)

class Provincia(models.Model):
	# SIMPLE FIELD
	nombre_provincia = models.CharField(max_length=100, verbose_name="Nombre")

	# RELATION FIELD
	region = models.ForeignKey(Region, verbose_name="Región")
	
	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "[%s] %s, %s" % (self.id, self.region.sigla_region, self.nombre_provincia)

class Comuna(models.Model):
	# SIMPLE FIELD
	nombre_comuna = models.CharField(max_length=100, verbose_name="Nombre")

	# RELATION FIELD
	provincia = models.ForeignKey(Provincia, verbose_name="Provincia")
	
	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")
	
	def __str__(self):
		return "%s - %s" % (self.provincia.region.sigla_region, self.nombre_comuna)

class TipoTag(models.Model):
	#SIMPLE FIELD
	nombre_tipo_tag = models.CharField(max_length=100, verbose_name="Nombre", null=True, blank=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s" % (self.nombre_tipo_tag)
		

class Tag(models.Model):
	# SIMPLE FIELD
	texto_tag = models.CharField(max_length=100, verbose_name="Tag", null=True, blank=True)

	# RELATION FIELD
	tipo_tag = models.ForeignKey(TipoTag, verbose_name="Tipo de Tag", null=True, blank=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")


	def __str__(self):
		return "%s" % (self.texto_tag)

class EstadoTour(models.Model):
	# SIMPLE FIELD
	nombre_estado_tour = models.CharField(max_length=100, verbose_name="Nombre", null=True, blank=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s" % (self.nombre_estado_tour)

class TipoTour(models.Model):
	# SIMPLE FIELD
	nombre_tipo_tour = models.CharField(max_length=100, verbose_name="Nombre", null=True, blank=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s" % (self.nombre_tipo_tour)	
	
class TipoGuia(models.Model):
	# SIMPLE FIELD
	nombre_tipo_guia = models.CharField(max_length=100, verbose_name="Nombre", null=True, blank=True)
		
	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s" % (self.nombre_tipo_guia)

class RegistroGuia(models.Model):
	# SIMPLE FIELD
	direccion_guia_registro = models.CharField(max_length=255, verbose_name="Dirección Guia", null=True, blank=True)
	direccion_representante_legal_registro = models.CharField(max_length=255, verbose_name="Dirección Representante legal", null=True, blank=True)
	razon_social_guia_registro = models.CharField(max_length=255, verbose_name="Razón social", null=True, blank=True)
	representante_legal_guia_registro = models.CharField(max_length=255, verbose_name="Representante legal", null=True, blank=True)
	nombre_fantasia_guia_registro = models.CharField(max_length=255, verbose_name="Nombre", null=True, blank=True)
	es_sello_q_registro = models.BooleanField(default=False, verbose_name="¿Tiene sello Q?", blank=True)
	tipo_sello_q_registro = models.CharField(max_length=255, verbose_name="Tipo sello", null=True, blank=True)
	inicio_sello_q_registro = models.DateTimeField(verbose_name="Fecha inicio sello Q", null=True, blank=True)
	fin_sello_q_registro = models.DateTimeField(verbose_name="Fecha fin sello Q", null=True, blank=True)
	tipo_personalidad_registro = models.CharField(max_length=255, verbose_name="Personalidad Jurídica", null=True, blank=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s" % (self.nombre_fantasia_guia_registro)

class Guia(models.Model):
	# SIMPLE FIELD
	descripcion_guia = models.TextField(max_length=400, verbose_name="Descripción Guia", blank=True, null=True)
	clasificacion_guia = models.CharField(max_length=100, verbose_name="Clasificación", null=True, blank=True)
	rut_guia = models.CharField(max_length=100, verbose_name="Rut", null=True, blank=True)
	telefono_guia = models.CharField(max_length=100, verbose_name="Teléfono guia", null=True, blank=True)
	celular_guia = models.CharField(max_length=100, verbose_name="Celular guia", null=True, blank=True)

	# RELATION FIELD
	tags = models.ManyToManyField(Tag, related_name="guia", verbose_name="Tags guía", blank=True)
	tipos_guia = models.ManyToManyField(TipoGuia, related_name="guia", verbose_name="Tipos guía", blank=True)
	registro = models.OneToOneField(RegistroGuia, related_name="guia", verbose_name="Registro guía", blank=True, null=True)
	usuario = models.OneToOneField(auth.models.User, verbose_name="Usuario", null=True, blank=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s" % (self.descripcion_guia)

	
class Tour(models.Model):
	# SIMPLE FIELD
	nombre_tour = models.CharField(max_length=100, verbose_name="Nombre Tour", null=True, blank=True)
	descripcion_tour = models.TextField(max_length=400, verbose_name="Descripción Tour", blank=True, null=True)
	capacidad_tour = models.IntegerField(verbose_name="Capacidad Tour", null=True, blank=True) 
	precio_tour = models.IntegerField(verbose_name="Precio Tour", null=True, blank=True) 
	es_oferta = models.BooleanField(default=False, verbose_name="¿Tour en oferta?", blank=True)

	# RELATION FIELD
	tipo_tour = models.ForeignKey(TipoTour, verbose_name="Tipo tour", null=True, blank=True) 
	estado_tour = models.ForeignKey(EstadoTour, verbose_name="Estado Tour", null=True, blank=True)
	comunas = models.ManyToManyField(Comuna, related_name="tour", verbose_name="Comunas tour", blank=True)
	tags = models.ManyToManyField(Tag, related_name="tour", verbose_name="Tags tour", blank=True)
	guia = models.ForeignKey(Guia, related_name="tour", null=True, blank=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s" % (self.nombre_tour)
		
class Horario(models.Model):
	# SIMPLE FIELD
	inicio_horario = models.DateTimeField(verbose_name="Fecha inicio", null=True, blank=True)
	fin_horario = models.DateTimeField(verbose_name="Fecha fin", null=True, blank=True)

	# RELATION FIELD
	tour = models.ForeignKey(Tour, verbose_name="Horario Tour", null=True, blank=True)
	
	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "Inicio %s - Fin %s" % (str(self.inicio_horario),str(self.fin_horario))

class Pais(models.Model):
	# SIMPLE FIELD
	nombre_pais = models.CharField(max_length=255, verbose_name="Nombre", null=True, blank=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s" % (self.nombre_pais)

class Turista(models.Model):
	# SIMPLE FIELD
	descripcion_turista = models.TextField(max_length=400, verbose_name="Descripción Turista", blank=True, null=True)

	# RELATION FIELD
	usuario = models.OneToOneField(auth.models.User, verbose_name="usuario", blank=True, null=True)
	pais = models.ForeignKey(Pais, verbose_name="Pais", blank=True, null=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")
	
	def __str__(self):
		return "%s" % (self.descripcion_turista)	


class Actividad(models.Model):
	# SIMPLE FIELD
	nombre_actividad = models.CharField(max_length=100, verbose_name="Nombre", null=True, blank=True)
	descripcion_actividad = models.TextField(max_length=400, verbose_name="Descripción actividad", blank=True, null=True)

	# RELATION FIELD
	usuario = models.ForeignKey(auth.models.User, verbose_name="Usuario", null=True, blank=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s" % (self.descripcion_actividad)

class Rol(models.Model):
	# SIMPLE FIELD
	nombre_rol = models.CharField(max_length=100, verbose_name="Nombre", null=True, blank=True)

	# RELATION FIELD
	usuario = models.ManyToManyField(auth.models.User, verbose_name="Roles", blank=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s" % (self.nombre_rol)

class TextoSelect(models.Model):
	# SIMPLE FIELD
	categoria_texto_select = models.CharField(max_length=100, verbose_name="Categoría", null=True, blank=True)
	texto_select = models.CharField(max_length=100, verbose_name="Texto", null=True, blank=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "[%s][%s]" % (self.categoria_texto_select, self.texto_select)

class Evaluacion(models.Model):
	# SIMPLE FIELD
	puntuacion_tiempo_evaluacion = models.IntegerField(default=0, verbose_name="Puntuación tiempo", null=True, blank=True)
	puntuacion_calidad_evaluacion = models.IntegerField(default=0, verbose_name="Puntuación calidad", null=True, blank=True)
	puntuacion_cumplimiento_evaluacion = models.IntegerField(default=0, verbose_name="Puntuación cumplimiento", null=True, blank=True)
	comentario_evaluacion = models.TextField(max_length=400, verbose_name="Comentario", blank=True, null=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s" % (self.comentario_evaluacion)

class TipoMultimedia(models.Model):
	# SIMPLE FIELD
	nombre_tipo_multimedia = models.CharField(max_length=100, verbose_name="Nombre", null=True, blank=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s" % (self.nombre_tipo_multimedia)

class Multimedia(models.Model):
	# SIMPLE FIELD
	nombre_multimedia = models.CharField(max_length=100, verbose_name="Nombre", null=True, blank=True)
	descripcion_multimedia = models.TextField(max_length=400, verbose_name="Descripción", null=True, blank=True)
	formato_multimedia = models.CharField(max_length=100, verbose_name="Formato", null=True, blank=True)
	archivo_multimedia = models.FileField(verbose_name="Archivo multimedia" ,upload_to='documentos/multimedia/%Y/%m/%d', null=True, blank=True)

	# RELATION FIELD
	tour = models.ForeignKey(Tour, verbose_name="Tour", null=True, blank=True)
	tipo_multimedia = models.ForeignKey(TipoMultimedia, verbose_name="Tipo multimedia", null=True, blank=True)
	usuario = models.ForeignKey(auth.models.User, verbose_name="Usuario", null=True, blank=True)
	actividad = models.ForeignKey(Actividad, verbose_name="Actividad", null=True, blank=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s" % (self.nombre_multimedia)



class Staff(models.Model):
	# SIMPLE FIELD
	descripcion_staff = models.TextField(max_length=400, verbose_name="Descripción", null=True, blank=True)
	cargo_staff = models.CharField(max_length=255, verbose_name="Cargo Staff", null=True, blank=True)

	# RELATION FIELD
	usuario = models.OneToOneField(auth.models.User, verbose_name="usuario", blank=True, null=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s" % (self.descripcion_staff)



class Favorito(models.Model):
	# SIMPLE FIELD
	tipo_favorito = models.CharField(max_length=255, verbose_name="Tipo", null=True, blank=True)

	# RELATION FIELD
	turista = models.ForeignKey(Turista, verbose_name="Turista", blank=True, null=True)
	tour = models.ForeignKey(Tour, verbose_name="Tour", blank=True, null=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s" % (self.tipo_favorito)

class Suscripcion(models.Model):
	# RELATION FIELD
	usuario_seguidor = models.ForeignKey(auth.models.User, related_name="seguidor", verbose_name="Seguidor", null=True, blank=True)
	usuario_seguido = models.ForeignKey(auth.models.User, related_name="seguido", verbose_name="Seguido", null=True, blank=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

class Transaccion(models.Model):
	# SIMPLE FIELD
	monto_transaccion = models.IntegerField(default=0, verbose_name="Monto transacción", null=True, blank=True)
	codigo_transaccion = models.CharField(max_length=255, verbose_name="Código transacción", null=True, blank=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s" % (self.codigo_transaccion)

class InstanciaTour(models.Model):
	# SIMPLE FIELD
	inicio_instancia_tour = models.DateTimeField(verbose_name="Fecha inicio", null=True, blank=True)
	fin_instancia_tour = models.DateTimeField(verbose_name="Fecha fin", null=True, blank=True)
	cupo_instancia_tour = models.IntegerField(default=0, verbose_name="Cupo instancia tour", null=True, blank=True)
	costo_instacia_tour = models.IntegerField(default=0, verbose_name="Costo", null=True, blank=True)
	estado_instacia_tour = models.CharField(max_length=225, verbose_name="Estado instancia", null=True, blank=True)

	# RELATION FIELD
	tour = models.ForeignKey(Tour, verbose_name="Tour", null=True, blank=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s" % (self.cupo_instancia_tour)

class Inscripcion(models.Model):
	# SIMPLE FIELD
	cupo_inscripcion = models.IntegerField(default=0, verbose_name="Cupo inscripción", null=True, blank=True)
	costo_inscripcion = models.IntegerField(default=0, verbose_name="Costo", null=True, blank=True)
	terminos_servicio = models.CharField(max_length=255, verbose_name="Terminos", null=True, blank=True)

	# RELATION FIELD
	turista = models.ForeignKey(Turista, verbose_name="Turista", null=True, blank=True)
	transaccion = models.OneToOneField(Transaccion, related_name="transacción", verbose_name="Transacción", null=True, blank=True)
	evaluacion = models.OneToOneField(Evaluacion, related_name="evaliación", verbose_name="Evaluación", null=True, blank=True)
	instancia_tour = models.ForeignKey(InstanciaTour, verbose_name="Instancia tour", null=True, blank=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s" % (self.cupo_inscripcion)

class TipoServicio(models.Model):
	#SIMPLE FIELD
	nombre_tipo_servicio = models.CharField(max_length=255, verbose_name="Nombre", null=True, blank=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s" % (self.nombre_tipo_servicio)
		
class ServicioTour(models.Model):
	#SIMPLE FIELD
	descripcion_servicio_tour = models.TextField(max_length=400, verbose_name="Descripción", null=True, blank=True)
	es_pago_servicio_tour = models.BooleanField(default=False, verbose_name="¿Tiene costo el servicio?", blank=True)
	costo_servicio_tour = models.IntegerField(default=0, verbose_name="Costo", null=True, blank=True)

	# RELATION FIELD
	tipo_servicio = models.ForeignKey(TipoServicio, verbose_name="Tipo servicio", null=True, blank=True)
	tour = models.ForeignKey(Tour, verbose_name="Tour", null=True, blank=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s" % (self.descripcion_servicio_tour)

				
class Comentario(models.Model):
	#SIMPLE FIELD
	texto_comentario = models.CharField(max_length=255, verbose_name="Comentario", null=True, blank=True)

	# RELATION FIELD
	usuario = models.ForeignKey(auth.models.User, verbose_name="Usuario que comenta", null=True, blank=True)
	tour = models.ForeignKey(Tour, verbose_name="Tour comentado", null=True, blank=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s" % (self.texto_comentario)
	
class MensajeContacto(models.Model):
	#SIMPLE FIELD
	nombre = models.CharField(max_length=255, verbose_name="Nombre", null=True, blank=True)
	email = models.CharField(max_length=255, verbose_name="Email", null=True, blank=True)
	asunto = models.CharField(max_length=255, verbose_name="Asunto", null=True, blank=True)
	mensaje = models.TextField(max_length=400, verbose_name="Mensaje", blank=True, null=True)

	# TIMESTAMP FIELD
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Fecha creación")
	updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha última modificación")

	def __str__(self):
		return "%s" % (self.asunto)