from django.contrib import admin

from apps.gestiones.models import Empresa, FranjaHoraria, PuntoAcceso

# Register your models here.
admin.site.register(Empresa)
admin.site.register(FranjaHoraria)
admin.site.register(PuntoAcceso)
