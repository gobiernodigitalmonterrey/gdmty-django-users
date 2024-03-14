#!-*- coding: utf-8 -*-
"""
Authentication backend for Django's Administration panel users based on email and password
This packages adds features such as group permissions and reCaptcha enterprise token verification.

This package is published as free software under the terms of the Apache License, Version 2.0. Is developed by
Dirección de Gobierno Digital of the Secretaría de Innovación y Gobierno Abierto of Municipality of Monterrey.

Authors: ['César Benjamín García Martínez <mathereall@gmail.com>', 'Miguel Angel Hernández Cortés
<miguelhdezc12@gmail.com>', 'César Guillermo Vázquez Álvarez <chechar.2001@gmail.com>']
Email: gobiernodigital@monterrey.gob.mx
GitHub: https://github.com/gobiernodigitalmonterrey/gdmty-drf-firebase-auth
Package: gdmty_django_users
PyPi: https://pypi.org/project/gdmty-django-users/
License: Apache 2.0

"""

from django.apps import AppConfig


class GdmtyDjangoUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gdmty-django-users'
