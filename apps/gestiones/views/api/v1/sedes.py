from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from apps.gestiones.models import PuntoAcceso
from apps.gestiones.serializers import PuntoAccesoModelSerializer, ValidarPermisoSerializer


class PuntoAccesoModelViewSet(ModelViewSet):
    queryset = PuntoAcceso.objects.all()
    serializer_class = PuntoAccesoModelSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'])
    def validar_permiso(self, request):
        serializer_punto_acceso = ValidarPermisoSerializer(data=request.GET)
        serializer_punto_acceso.is_valid(raise_exception=True)
        data = serializer_punto_acceso.data
        return Response(data)
