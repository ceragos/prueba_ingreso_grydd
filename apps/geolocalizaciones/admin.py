from django.contrib import admin

from apps.geolocalizaciones.models import Pais, Estado, Ciudad

# Register your models here.
admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Ciudad)
