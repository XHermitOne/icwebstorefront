# -*- coding: utf-8 -*-

from django.core.mail import EmailMultiAlternatives


def send_email(addr_from, addr_to, subject, body_text,
               email_headers={}):
    """
    Отправка письма.
    """
    message = EmailMultiAlternatives(subject, body_text, addr_from, [addr_to],
                                     headers=email_headers)

    message.send(fail_silently=False)