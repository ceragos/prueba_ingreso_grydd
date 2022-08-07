from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic.list import ListView

from apps.gestiones.models import FranjaHoraria
from apps.gestiones.forms import FranjaHorariaForm
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


class FranjaHorariaCreateView(CreateView):
    model = FranjaHoraria
    form_class = FranjaHorariaForm
    template_name = 'gestiones/horarios_acceso/crear.html'
    success_url = reverse_lazy('gestiones:sedes.listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Crear'
        context['nombre_empleado'] = f'{self.get_empleado().first_name} {self.get_empleado().last_name}'
        return context

    def get_empleado(self):
        pk_empleado = self.kwargs.get('pk_empleado')
        return Usuario.objects.filter(pk=pk_empleado).first()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        empleado = self.get_empleado()
        if empleado:
            kwargs['empleado'] = empleado
        return kwargs

    def get_success_url(self):
        return reverse_lazy('gestiones:horario_acceso.listar', args=[self.object.empleado.pk])


class FranjaHorariaUpdateView(UpdateView):
    model = FranjaHoraria
    form_class = FranjaHorariaForm
    template_name = 'gestiones/horarios_acceso/crear.html'
    success_url = reverse_lazy('gestiones:sedes.listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Editar'
        context['nombre_empleado'] = f'{self.object.empleado.first_name} {self.object.empleado.last_name}'
        return context

    def get_success_url(self):
        return reverse_lazy('gestiones:horario_acceso.listar', args=[self.object.empleado.pk])
