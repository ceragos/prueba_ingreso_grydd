from django.core.validators import RegexValidator

telefono_regex = RegexValidator(
    regex=r'\+?2?\d{9,15}$',
    message="El número de teléfono debe ingresarse en el formato: +999999999999. Se permiten hasta 15 dígitos."
)