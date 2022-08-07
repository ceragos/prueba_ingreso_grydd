from django.views.generic.list import ListView

from apps.gestiones.models import FranjaHoraria
from apps.usuarios.models import Usuario

class FranjaHorariaListView(ListView):
    model = FranjaHoraria
    context_object_name = 'franjas_horarias'
    template_name = 'gestiones/horarios_acceso/listar.html'
    paginate_by = 10

    def get_empleado(self):
        return Usuario.objects.filter(pk=self.kwargs.get('pk_empleado')).first()

    def get_queryset(self):
        return super().get_queryset().filter(empleado=self.get_empleado().pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre_empleado'] = f'{self.get_empleado().first_name} {self.get_empleado().last_name}'
        context['id_empleado'] = self.get_empleado().pk
        return context
