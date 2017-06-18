from rest_framework import serializers
from cicerotwebapp import models
from fcm_django import models as FCMModels
from django.contrib import auth 
from rest_framework import validators

import traceback
from rest_framework.utils import model_meta
from rest_framework.compat import set_many
from rest_framework.validators import UniqueTogetherValidator

class RegionSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Region
		fields= ('id','nombre_region','sigla_region', 'created_at', 'updated_at')

class ProvinciaSerializers(serializers.HyperlinkedModelSerializer):
	region = RegionSerializers(many=False, read_only=True)

	class Meta:
		model = models.Provincia
		fields = ('id', 'nombre_provincia', 'region', 'created_at', 'updated_at')

class ComunaSerializers(serializers.HyperlinkedModelSerializer):
	provincia = ProvinciaSerializers(many=False, read_only=True)

	class Meta:
		model = models.Comuna
		fields = ('id', 'nombre_comuna', 'provincia', 'created_at', 'updated_at')


class TipoTagSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.TipoTag
		fields = ('id', 'nombre_tipo_tag', 'created_at', 'updated_at')

class TagSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Tag
		fields = ('id' , 'texto_tag', 'created_at', 'updated_at')


class EstadoTourSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.EstadoTour
		fields = ('id', 'nombre_estado_tour', 'created_at', 'updated_at')
	

class TipoTourSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.TipoTour
		fields = ('id', 'nombre_tipo_tour', 'created_at', 'updated_at')
	
	
class TipoGuiaSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.TipoGuia
		fields = ('id', 'nombre_tipo_guia', 'created_at', 'updated_at')
	
class RegistroGuiaSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.RegistroGuia
		fields = ('id', 'direccion_guia_registro', 'direccion_representante_legal_registro',
				  'razon_social_guia_registro', 'representante_legal_guia_registro',
				  'nombre_fantasia_guia_registro', 'es_sello_q_registro', 'tipo_sello_q_registro',
				  'inicio_sello_q_registro', 'fin_sello_q_registro', 'tipo_personalidad_registro',
				  'created_at', 'updated_at')

class GuiaSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Guia
		fields = ('id', 'descripcion_guia', 'clasificacion_guia', 'rut_guia', 'telefono_guia',
		 		  'celular_guia', 'tipos_guia', 'registro', 'usuario', 'created_at', 'updated_at')

	
class TourSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Tour
		fields = ('id', 'nombre_tour', 'descripcion_tour', 'capacidad_tour', 'precio_tour',
				  'es_oferta', 'tipo_tour', 'estado_tour', 'comunas', 'tags', 'guia', 'created_at', 'updated_at')
	
		
class HorarioSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Horario
		fields = ('id', 'inicio_horario', 'fin_horario', 'created_at', 'updated_at')
	

class PaisSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Pais
		fields = ('id', 'nombre_pais')
	# SIMPLE FIELD
	

class TuristaSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Turista
		fields = ('id', 'descripcion_turista', 'usuario', 'pais', 'created_at', 'updated_at')
	

class ActividadSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Actividad
		fields = ('id', 'nombre_actividad', 'descripcion_actividad', 'usuario', 'created_at', 'updated_at')
	

class RolSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Rol
		fields = ('id', 'nombre_rol', 'usuario', 'created_at', 'updated_at')
	

class TextoSelectSerializers(serializers.HyperlinkedModelSerializer):
	class Meta: 
		model = models.TextoSelect
		fields = ('id', 'categoria_texto_select', 'texto_select', 'created_at', 'updated_at')
	

class EvaluacionSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Evaluacion
		fields = ('id', 'puntuacion_tiempo_evaluacion', 'puntuacion_calidad_evaluacion',
				  'puntuacion_cumplimiento_evaluacion', 'comentario_evaluacion', 'created_at', 'updated_at')

class TipoMultimediaSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.TipoMultimedia
		fields = ('id', 'nombre_tipo_multimedia', 'created_at', 'updated_at')

class MultimediaSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Multimedia
		fields = ('id', 'nombre_multimedia', 'descripcion_multimedia', 'formato_multimedia',
				  'archivo_multimedia', 'tour', 'tipo_multimedia', 'usuario', 'actividad',
				  'created_at', 'updated_at')
	
class StaffSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Staff
		fields = ('id', 'descripcion_staff', 'cargo_staff', 'usuario', 'created_at', 'updated_at')
	

class FavoritoSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Favorito 
		fields = ('id', 'tipo_favorito', 'turista', 'tour', 'created_at', 'updated_at')
	

class SuscripcionSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Suscripcion
		fields = ('id', 'usuario_seguidor', 'usuario_seguido', 'created_at', 'updated_at')


class TransaccionSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Transaccion
		fields = ('id', 'monto_transaccion', 'codigo_transaccion', 'created_at', 'updated_at')
	

class InstanciaTourSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.InstanciaTour
		fields = ('id', 'inicio_instancia_tour', 'fin_instancia_tour', 'cupo_instancia_tour',
				  'costo_instacia_tour', 'estado_instacia_tour', 'tour', 'created_at', 'updated_at')

	
class InscripcionSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Inscripcion
		fields = ('id', 'cupo_inscripcion', 'costo_inscripcion', 'terminos_servicio', 'turista',
				  'transaccion', 'evaluacion', 'instancia_tour', 'created_at', 'updated_at')


class TipoServicioSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.TipoServicio
		fields = ('id', 'nombre_tipo_servicio', 'created_at', 'updated_at')

		
class ServicioTourSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.ServicioTour
		fields = ('id', 'descripcion_servicio_tour', 'es_pago_servicio_tour', 'costo_servicio_tour',
				 'tipo_servicio', 'tour', 'created_at', 'updated_at')

				
class ComentarioSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Comentario
		fields = ('id', 'texto_comentario', 'usuario', 'tour', 'created_at', 'updated_at')
	
class FCMDeviceSerializers(serializers.ModelSerializer):
	class Meta:
		model = FCMModels.FCMDevice
		fields = ('id', 'name', 'active', 'device_id', 'registration_id', 'type', 'user')
		extra_kwargs = {
			'user': {'read_only': False},
			'name': {'read_only': False},
			'active': {'read_only': False},
			'device_id': {'read_only': False},
			'registration_id': {'read_only': False},
			'type': {'read_only': False},
		}	

		validators = [
           UniqueTogetherValidator(
                queryset=FCMModels.FCMDevice.objects.all(),
                fields=('device_id', ),
                message = 'Ya existe un usuario registrado con este dispositivo',
            )
        ]

