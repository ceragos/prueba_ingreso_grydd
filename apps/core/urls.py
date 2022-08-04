"""ERP URL Configuration

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

from apps.core.views import BlankTemplateView, IndexTemplateView, ButtonsTemplateView, PageNotFoundTemplateView, \
    CardsTemplateView, ChartsTemplateView, TablesTemplateView, UtilitiesColorTemplateView, UtilitiesBorderTemplateView, \
    UtilitiesAnimationsTemplateView, UtilitiesOtherTemplateView, LoginBasicTemplateView, RegisterTemplateView, \
    ForgotPasswordTemplateView, HomeTemplateView, FormsTemplateView, LoginSocialTemplateView, InvoiceTemplateView, \
    WizardTemplateView

urlpatterns = [
    path('', login_required(HomeTemplateView.as_view()), name='core.home'),
    path('index/', IndexTemplateView.as_view(), name='core.index'),
    path('components/buttons/', ButtonsTemplateView.as_view(), name='core.buttons'),
    path('components/cards/', CardsTemplateView.as_view(), name='core.cards'),
    path('components/forms/', FormsTemplateView.as_view(), name='core.forms'),
    path('utilities/color/', UtilitiesColorTemplateView.as_view(), name='core.utilities_color'),
    path('utilities/border/', UtilitiesBorderTemplateView.as_view(), name='core.utilities_border'),
    path('utilities/animations/', UtilitiesAnimationsTemplateView.as_view(), name='core.utilities_animations'),
    path('utilities/other/', UtilitiesOtherTemplateView.as_view(), name='core.utilities_other'),
    path('login_basic/', LoginBasicTemplateView.as_view(), name='core.login_basic'),
    path('login_social/', LoginSocialTemplateView.as_view(), name='core.login_social'),
    path('register/', RegisterTemplateView.as_view(), name='core.register'),
    path('forgot_password/', ForgotPasswordTemplateView.as_view(), name='core.forgot_password'),
    path('pages/404/', PageNotFoundTemplateView.as_view(), name='core.404'),
    path('pages/blank/', BlankTemplateView.as_view(), name='core.blank'),
    path('pages/invoice/', InvoiceTemplateView.as_view(), name='core.invoice'),
    path('flows/wizard/', WizardTemplateView.as_view(), name='core.wizard'),
    path('charts/', ChartsTemplateView.as_view(), name='core.charts'),
    path('tables/', TablesTemplateView.as_view(), name='core.tables'),
]
