from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from apps.geolocalizaciones.models import Pais, Estado, Ciudad

# Register your models here.
@admin.register(Pais)
class PaisAdmin(ImportExportModelAdmin):
    pass


@admin.register(Estado)
class EstadoAdmin(ImportExportModelAdmin):
    pass


@admin.register(Ciudad)
class CiudadAdmin(ImportExportModelAdmin):
    pass
