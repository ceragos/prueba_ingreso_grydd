from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = BASE_DIR / "sent_emails"

# Para generar el modelado del projecto ejecuta el siguiente comando
# python manage.py graph_models -a > my_project.dot
GRAPH_MODELS = {
    'all_aplications': True,
    'group_models': True,
}
# Para convertir el archivo .dot en imagen png ingrese al siguiente sitio web
# https://onlineconvertfree.com/es/convert-format/dot-to-png/
