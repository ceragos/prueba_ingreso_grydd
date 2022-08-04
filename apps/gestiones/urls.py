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

from apps.gestiones.views import EmpresaCreateView, EmpresaListView, PuntoAccesoCreateView, PuntoAccesoListView

urlpatterns = [
    path('empresas/listar/', login_required(EmpresaListView.as_view()), name='empresas.listar'),
    path('empresas/crear/', login_required(EmpresaCreateView.as_view()), name='empresas.crear'),

    path('sedes/listar/', login_required(PuntoAccesoListView.as_view()), name='sedes.listar'),
    path('sedes/crear/', login_required(PuntoAccesoCreateView.as_view()), name='sedes.crear'),
]
