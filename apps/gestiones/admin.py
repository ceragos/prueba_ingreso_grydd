from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from apps.gestiones.models import Empresa, FranjaHoraria, PuntoAcceso

# Register your models here.
@admin.register(Empresa)
class EmpresaAdmin(ImportExportModelAdmin):
    pass


@admin.register(FranjaHoraria)
class FranjaHorariaAdmin(ImportExportModelAdmin):
    pass


@admin.register(PuntoAcceso)
class PuntoAccesoAdmin(ImportExportModelAdmin):
    pass
