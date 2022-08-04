from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'core/home.html'


class IndexTemplateView(TemplateView):
    template_name = 'core/startbootstrap/index.html'


class ButtonsTemplateView(TemplateView):
    template_name = 'core/startbootstrap/buttons.html'


class CardsTemplateView(TemplateView):
    template_name = 'core/startbootstrap/cards.html'


class FormsTemplateView(TemplateView):
    template_name = 'core/startbootstrap/forms.html'


class UtilitiesColorTemplateView(TemplateView):
    template_name = 'core/startbootstrap/utilities-color.html'


class UtilitiesBorderTemplateView(TemplateView):
    template_name = 'core/startbootstrap/utilities-border.html'


class UtilitiesAnimationsTemplateView(TemplateView):
    template_name = 'core/startbootstrap/utilities-animations.html'


class UtilitiesOtherTemplateView(TemplateView):
    template_name = 'core/startbootstrap/utilities-other.html'


class LoginBasicTemplateView(TemplateView):
    template_name = 'core/startbootstrap/login_basic.html'


class LoginSocialTemplateView(TemplateView):
    template_name = 'core/startbootstrap/login_social.html'


class RegisterTemplateView(TemplateView):
    template_name = 'core/startbootstrap/register.html'


class ForgotPasswordTemplateView(TemplateView):
    template_name = 'core/startbootstrap/forgot-password.html'


class PageNotFoundTemplateView(TemplateView):
    template_name = 'core/startbootstrap/404.html'


class BlankTemplateView(TemplateView):
    template_name = 'core/startbootstrap/blank.html'


class InvoiceTemplateView(TemplateView):
    template_name = 'core/startbootstrap/invoice.html'


class WizardTemplateView(TemplateView):
    template_name = 'core/startbootstrap/wizard.html'


class ChartsTemplateView(TemplateView):
    template_name = 'core/startbootstrap/charts.html'


class TablesTemplateView(TemplateView):
    template_name = 'core/startbootstrap/tables.html'
