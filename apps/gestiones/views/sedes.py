from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic.list import ListView

from apps.gestiones.models import PuntoAcceso
from apps.gestiones.forms import PuntoAccesoForm


class PuntoAccesoListView(ListView):
    model = PuntoAcceso
    context_object_name = 'puntos_acceso'
    template_name = 'gestiones/puntos_acceso/listar.html'
    paginate_by = 10


class PuntoAccesoCreateView(CreateView):
    model = PuntoAcceso
    form_class = PuntoAccesoForm
    template_name = 'gestiones/puntos_acceso/crear.html'
    success_url = reverse_lazy('gestiones:sedes.listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Crear'
        return context


class PuntoAccesoUpdateView(UpdateView):
    model = PuntoAcceso
    form_class = PuntoAccesoForm
    template_name = 'gestiones/puntos_acceso/crear.html'
    success_url = reverse_lazy('gestiones:sedes.listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Editar'
        return context
