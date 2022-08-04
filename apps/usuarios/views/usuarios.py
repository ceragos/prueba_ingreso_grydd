from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.list import ListView

from apps.usuarios.models import Usuario
from apps.usuarios.forms import UsuarioAdministradorForm, UsuarioForm


class UsuarioAdministradorListView(ListView):
    model = Usuario
    context_object_name = 'administradores'
    template_name = 'usuarios/administradores/listar.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_staff=True)
        return queryset


class UsuarioAdministradorCreateView(CreateView):
    model = Usuario
    form_class = UsuarioAdministradorForm
    template_name = 'usuarios/administradores/crear.html'
    success_url = reverse_lazy('usuarios:administradores.listar')


class UsuarioEmpleadoListView(ListView):
    model = Usuario
    context_object_name = 'empleados'
    template_name = 'usuarios/empleados/listar.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_staff=False)
        return queryset


class UsuarioEmpleadoCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/empleados/crear.html'
    success_url = reverse_lazy('usuarios:empleados.listar')
