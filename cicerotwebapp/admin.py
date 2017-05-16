from django.contrib import admin
from cicerotwebapp import models
# Register your models here.

class RegionAdmin(admin.ModelAdmin):
	list_display = ('nombre_region', 'sigla_region', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class ProvinciaAdmin(admin.ModelAdmin):
	list_display = ('nombre_provincia', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class ComunaAdmin(admin.ModelAdmin):
	list_display = ('nombre_comuna', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class TipoTagAdmin(admin.ModelAdmin):
	list_display = ('nombre_tipo_tag', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class TagAdmin(admin.ModelAdmin):
	list_display = ('texto_tag', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class EstadoTourAdmin(admin.ModelAdmin):
	list_display = ('nombre_estado_tour', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class TipoTourAdmin(admin.ModelAdmin):
	list_display = ('nombre_tipo_tour', 'created_at', 'updated_at') 
	list_filter = ['created_at', 'updated_at']
		
class TipoGuiaAdmin(admin.ModelAdmin):
	list_display = ('nombre_tipo_guia', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class RegistroGuiaAdmin(admin.ModelAdmin):
	list_display = ('razon_social_guia_registro', 'nombre_fantasia_guia_registro', 'es_sello_q_registro', 'created_at', 'updated_at')
	list_filter = ['es_sello_q_registro', 'created_at', 'updated_at']

class GuiaAdmin(admin.ModelAdmin):
	list_display = ('rut_guia', 'clasificacion_guia', 'telefono_guia', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class TourAdmin(admin.ModelAdmin):
	list_display = ('nombre_tour', 'capacidad_tour', 'precio_tour', 'es_oferta', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class HorarioAdmin(admin.ModelAdmin):
	list_display = ('inicio_horario', 'fin_horario', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class PaisAdmin(admin.ModelAdmin):
	list_display = ('nombre_pais', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class TuristaAdmin(admin.ModelAdmin):
	list_display = ('descripcion_turista', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class ActividadAdmin(admin.ModelAdmin):
	list_display = ('nombre_actividad', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']	

class RolAdmin(admin.ModelAdmin):
	list_display = ('nombre_rol', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class TextoSelectAdmin(admin.ModelAdmin):
	list_display = ('categoria_texto_select', 'texto_select', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class EvaluacionAdmin(admin.ModelAdmin):
	list_display = ('puntuacion_tiempo_evaluacion', 'puntuacion_calidad_evaluacion', 'puntuacion_cumplimiento_evaluacion', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class TipoMultimediaAdmin(admin.ModelAdmin):
	list_display = ('nombre_tipo_multimedia', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class MultimediaAdmin(admin.ModelAdmin):
	list_display = ('nombre_multimedia', 'formato_multimedia', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class StaffAdmin(admin.ModelAdmin):
	list_display = ('cargo_staff', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class FavoritoAdmin(admin.ModelAdmin):
	list_display = ('tipo_favorito', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class SuscripcionAdmin(admin.ModelAdmin):
	list_display = ('usuario_seguidor', 'usuario_seguido', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class TransaccionAdmin(admin.ModelAdmin):
	list_display = ('monto_transaccion', 'codigo_transaccion', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class InstanciaTourAdmin(admin.ModelAdmin):
	list_display = ('inicio_instancia_tour', 'fin_instancia_tour', 'cupo_instancia_tour', 'estado_instacia_tour', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class InscripcionAdmin(admin.ModelAdmin):
	list_display = ('costo_inscripcion', 'cupo_inscripcion', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class TipoServicioAdmin(admin.ModelAdmin):
	list_display = ('nombre_tipo_servicio', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']

class ServicioTourAdmin(admin.ModelAdmin):
	list_display = ('descripcion_servicio_tour', 'es_pago_servicio_tour', 'tipo_servicio', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at', 'tipo_servicio']
		
class ComentarioAdmin(admin.ModelAdmin):
	list_display = ('texto_comentario', 'created_at', 'updated_at')
	list_filter = ['created_at', 'updated_at']


admin.site.register(models.Region, RegionAdmin)
admin.site.register(models.Provincia, ProvinciaAdmin)
admin.site.register(models.Comuna, ComunaAdmin)
admin.site.register(models.TipoTag, TipoTagAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.EstadoTour, EstadoTourAdmin)
admin.site.register(models.TipoTour, TipoTourAdmin)
admin.site.register(models.TipoGuia, TipoGuiaAdmin)
admin.site.register(models.RegistroGuia, RegistroGuiaAdmin)
admin.site.register(models.Guia, GuiaAdmin)
admin.site.register(models.Tour, TourAdmin)
admin.site.register(models.Horario, HorarioAdmin)
admin.site.register(models.Pais, PaisAdmin)
admin.site.register(models.Turista, TuristaAdmin)
admin.site.register(models.Actividad, ActividadAdmin)
admin.site.register(models.Rol, RolAdmin)
admin.site.register(models.TextoSelect, TextoSelectAdmin)
admin.site.register(models.Evaluacion, EvaluacionAdmin)
admin.site.register(models.TipoMultimedia, TipoMultimediaAdmin)
admin.site.register(models.Multimedia, MultimediaAdmin)
admin.site.register(models.Staff, StaffAdmin)
admin.site.register(models.Favorito, FavoritoAdmin)
admin.site.register(models.Suscripcion, SuscripcionAdmin)
admin.site.register(models.Transaccion, TransaccionAdmin)
admin.site.register(models.InstanciaTour, InstanciaTourAdmin)
admin.site.register(models.Inscripcion, InscripcionAdmin)
admin.site.register(models.TipoServicio, TipoServicioAdmin)
admin.site.register(models.ServicioTour, ServicioTourAdmin)
admin.site.register(models.Comentario, ComentarioAdmin)
