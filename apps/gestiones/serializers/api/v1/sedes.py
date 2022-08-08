from datetime import datetime
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from apps.gestiones.models import PuntoAcceso
from apps.usuarios.models import Usuario

class PuntoAccesoModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = PuntoAcceso
        fields = [
            'id', 'nombre', 'direccion', 'email', 'empresa', 'geolocalizacion', 'is_active'
        ]
        read_only_fields = fields

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['empresa'] = instance.empresa.nombre
        return data


class ValidarPermisoSerializer(serializers.Serializer):
    email_empleado = serializers.EmailField()
    punto_acceso = serializers.PrimaryKeyRelatedField(queryset=PuntoAcceso.objects.all())

    def validate_email_empleado(self, value):
        usuario = Usuario.objects.filter(email=value).first()
        if not usuario:
            raise ValidationError(f'Email no válido \"{value}\": el empleado no existe.')
        return usuario
    
    def to_representation(self, instance):
        
        data = self.validated_data
        empleado = data['email_empleado']
        punto_acceso = data['punto_acceso']
        horarios_acceso = punto_acceso.horarios_acceso.all()
        hora_actual = datetime.now().time()
        horarios_acceso = horarios_acceso.filter(empleado=empleado, hora_inicio__lte=hora_actual, hora_finalizacion__gte=hora_actual, is_active=True)
        
        acceso = bool(horarios_acceso) and punto_acceso.is_active
        data_punto_acceso = PuntoAccesoModelSerializer(punto_acceso)
        data = {
            'acceso': acceso,
            'franja': repr(horarios_acceso.first()),
            'punto_acceso': data_punto_acceso.data
        }
        return data
