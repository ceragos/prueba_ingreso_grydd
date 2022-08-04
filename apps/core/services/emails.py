from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def email():
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['antonio.casta_yo@hotmail.com',]

    html_message = render_to_string(
        'core/startbootstrap/email.html'
    )
    message = strip_tags(html_message)

    send_mail( subject, message, email_from, recipient_list, html_message=html_message)
