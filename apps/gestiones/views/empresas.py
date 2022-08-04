from django.urls import reverse_lazy
from django.views.generic import CreateView
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
