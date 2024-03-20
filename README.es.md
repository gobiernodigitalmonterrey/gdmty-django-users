# gdmty-django-users

Este es un proyecto personalizado de backend de autenticación de Django Rest Framework llamado `gdmty-django-users`.
Está diseñado para autenticar usuarios en el panel de administración basado en correo electrónico y contraseña, con
verificación de token de reCaptcha.

El proyecto es mantenido por el Gobierno de Monterrey. Puedes encontrar más información sobre el proyecto en
su [página principal](https://github.com/gobiernodigitalmonterrey/gdmty-django-users) o reportar problemas en
el [rastreador de errores](https://github.com/gobiernodigitalmonterrey/gdmty-django-users/issues).

## Características

- Autenticación basada en correo electrónico y contraseña para usuarios en el panel de administración.
- Verificación de token de reCaptcha para mayor seguridad.
- Compatibilidad con Python 3.9 o posterior, y Django 4.1.13 o posterior.

## Instalación

```bash
$ pip install gdmty-django-users
```

## Configuración

Agrega la aplicación a `INSTALLED_APPS` de tu proyecto en `settings.py` ademas de agregar la variable DRF_ROUTER.

```python
from rest_framework import routers

INSTALLED_APPS = [
    # ...
    'gdmty_django_users',
    ...
]
DRF_ROUTER = routers.DefaultRouter()  # Necesario para el paquete gdmty_django_users
```

Ejemplo de uso en tu archivo 'models.py:

```python 
from gdmty_django_users.models import User
from django.db import models


class MyModel(models.Model):
    user = User.ForeignKey(User, on_delete=User.CASCADE)
```

## Contribuyendo

* Por favor, levanta un problema/función y nombra tu rama 'feature-n' o 'issue-n', donde 'n' es el número del problema.
* Si pruebas este código con una versión de Python no listada arriba y todo va bien, por favor haz un fork y actualiza
  el README para incluir la versión de Python que usaste :)

## Notas adicionales

* Este proyecto es mantenido por el Gobierno de Monterrey.
* La página principal del proyecto está [aquí](https://github.com/gobiernodigitalmonterrey/gdmty-django-users) y los
  problemas pueden ser reportados [aquí](https://github.com/gobiernodigitalmonterrey/gdmty-django-users/issues).