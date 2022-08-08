from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic.list import ListView

from apps.gestiones.models import Empresa
from apps.gestiones.forms import EmpresaForm


class EmpresaListView(ListView):
    model = Empresa
    context_object_name = 'empresas'
    template_name = 'gestiones/empresas/listar.html'
    paginate_by = 10


class EmpresaCreateView(CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'gestiones/empresas/crear.html'
    success_url = reverse_lazy('gestiones:empresas.listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Crear'
        return context
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        point_map_center = self.request.GET.get('point_map_center')
        if point_map_center:
            kwargs['point_map_center'] = point_map_center
        return kwargs


class EmpresaUpdateView(UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'gestiones/empresas/crear.html'
    success_url = reverse_lazy('gestiones:empresas.listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Editar'
        return context
