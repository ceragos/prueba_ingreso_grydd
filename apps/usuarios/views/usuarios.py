import jwt
from django.conf import settings
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView, TemplateView
from django.views.generic.list import ListView

from apps.gestiones.models import Empresa
from apps.usuarios.models import Usuario
from apps.usuarios.forms import UsuarioAdministradorForm, UsuarioForm, EstablecerContrasenaFrom, InvitarEmpleadoFrom


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

    def get_empresa(self):
        pk_empresa = self.kwargs.get('pk_empresa')
        return Empresa.objects.filter(pk=pk_empresa).first()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        point_map_center = self.request.GET.get('point_map_center')
        if point_map_center:
            kwargs['point_map_center'] = point_map_center
        empresa = self.get_empresa()
        if empresa:
            kwargs['empresa'] = empresa
        return kwargs

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()

        # Si el usuario es creado desde la sección de empresas se agrega update_fiels para
        # ejecutar la validacion del signal postsave que realiza la invitación por correo electronico
        empresa = self.get_empresa()
        if empresa:
            empresa.administrador = self.object
            update_fields = ['administrador']
            empresa.save(update_fields=update_fields)
        return super().form_valid(form)


class ValidarInvitacionRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        token = self.kwargs.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            administrador = payload['administrador']
        except:
            return reverse_lazy('usuarios:administradores.invitacion_invalida')

        if payload['tipo'] != 'invitacion_administrador':
            return reverse_lazy('usuarios:administradores.invitacion_invalida')

        usuario = Usuario.objects.filter(email=administrador).first()
        if not usuario.password:
            return reverse_lazy('usuarios:usuario.establecer_contrasena', args=[administrador])
        raise Http404


class InvitacionInvalidaTemplateView(TemplateView):
    template_name = 'usuarios/invitacion_invalida.html'


class EstablecerContrasenaFormView(FormView):
    template_name = 'usuarios/establecer_contrasena.html'
    form_class = EstablecerContrasenaFrom
    success_url = reverse_lazy('core:core.home')
    
    def get(self, request, *args, **kwargs):
        usuario = self.get_email_usuario()
        if usuario.password:
            return HttpResponseRedirect(reverse_lazy('core:core.home'))
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_email_usuario(self):
        email = self.kwargs.get('email')
        return Usuario.objects.filter(email=email).first()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        email = self.get_email_usuario()
        if email:
            kwargs['email'] = email
        return kwargs


class UsuarioEmpleadoListView(ListView):
    model = Usuario
    context_object_name = 'empleados'
    template_name = 'usuarios/empleados/listar.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        empresa = self.request.user.empresa
        queryset = queryset.filter(is_staff=False, empresa=empresa)
        return queryset


class UsuarioEmpleadoCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/empleados/crear.html'
    success_url = reverse_lazy('usuarios:empleados.listar')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        point_map_center = self.request.GET.get('point_map_center')
        if point_map_center:
            kwargs['point_map_center'] = point_map_center
        return kwargs


class InvitarEmpleadoFormView(FormView):
    template_name = 'usuarios/empleados/invitar.html'
    form_class = InvitarEmpleadoFrom
    success_url = reverse_lazy('core:core.home')


class UsuarioEmpleadoRegistrarView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/empleados/registrar.html'
    success_url = reverse_lazy('core:core.home')

    def get_success_url(self):
        return reverse_lazy('usuarios:empleados.registro_exitoso')

    def get_empresa(self):
        empresa = self.kwargs.get('pk_empresa')
        return Empresa.objects.filter(pk=empresa).first()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        empresa = self.get_empresa()
        if empresa:
            kwargs['empresa'] = empresa
        return kwargs


class RegistroExitosoTemplateView(TemplateView):
    template_name = 'usuarios/empleados/registro_exitoso.html'
