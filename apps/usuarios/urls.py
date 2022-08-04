"""GRYDD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.usuarios.views import UsuarioAdministradorListView, UsuarioAdministradorCreateView, UsuarioEmpleadoListView, \
    UsuarioEmpleadoCreateView

urlpatterns = [
    path('administradores/listar/', login_required(UsuarioAdministradorListView.as_view()), name='administradores.listar'),
    path('administradores/crear/', login_required(UsuarioAdministradorCreateView.as_view()), name='administradores.crear'),

    path('empleados/listar/', login_required(UsuarioEmpleadoListView.as_view()), name='empleados.listar'),
    path('empleados/crear/', login_required(UsuarioEmpleadoCreateView.as_view()), name='empleados.crear'),
]