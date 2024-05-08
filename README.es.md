# gdmty-django-users

La aplicación `gdmty-django-users`es un paquete de Django que extiende la clase abstracta AbstractBaseUser para usar el correo electrónico como usuario. Y tiene la opción de autenticar con verificación de token reCaptcha.

El proyecto es mantenido por el Gobierno de Monterrey. Puedes encontrar más información sobre el proyecto en
su [página principal](https://github.com/gobiernodigitalmonterrey/gdmty-django-users) o reportar problemas en
el [rastreador de errores](https://github.com/gobiernodigitalmonterrey/gdmty-django-users/issues).

## Características

- Identificación de usuarios basada en el correo electrónico: Utiliza direcciones de correo electrónico como identificadores de usuario.
- Modelo de usuario personalizado: Extiende el AbstractBaseUser de Django para proporcionar funcionalidad de usuario personalizada.
- Diseño modular: Diseñado como una aplicación Django reutilizable para una fácil integración en diferentes proyectos.
- Compatible con Python 3.9 o posterior, y Django 4.1.13 o posterior.

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

* Por favor, levanta un problema/feature y nombra tu rama 'feature-n' o 'issue-n', donde 'n' es el número del problema.
* Si pruebas este código con una versión de Python o una paqueteria no listada arriba y todo va bien, por favor haz un fork y actualiza
  el README para incluir la versión de Python que usaste :)

## Notas adicionales

* Este proyecto es mantenido por el Gobierno de Monterrey.
* La página principal del proyecto está [aquí](https://github.com/gobiernodigitalmonterrey/gdmty-django-users) y los
  problemas pueden ser reportados [aquí](https://github.com/gobiernodigitalmonterrey/gdmty-django-users/issues).
