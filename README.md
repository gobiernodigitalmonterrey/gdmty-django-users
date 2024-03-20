# gdmty-django-users

This is a custom Django Rest Framework authentication backend project named `gdmty-django-users`. It is designed to
authenticate users in the Administration panel based on email and password, with reCaptcha token verification.

The project is maintained by Gobierno de Monterrey. You can find more about the project on
its [homepage](https://github.com/gobiernodigitalmonterrey/gdmty-django-users) or report issues on
the [bug tracker](https://github.com/gobiernodigitalmonterrey/gdmty-django-users/issues).

## Features

- Email and password-based authentication for users in the Administration panel.
- reCaptcha token verification for added security.
- Compatibility with Python 3.9 and later, and Django 4.1.13 and later.

## Installation

```bash
$ pip install gdmty-django-users
```

## Configuration

Add the application to your project's `INSTALLED_APPS` in `settings.py` also add the DRF_ROUTER variable.

```python
from rest_framework import routers

INSTALLED_APPS = [
    # ...
    'gdmty_django_users',
    ...
]
DRF_ROUTER = routers.DefaultRouter()  # Necessary for the gdmty_django_users package

```

An example to use in your 'models.py file:

    ```python 
    from gdmty_django_users.models import User

    from django.db import models

    class MyModel(models.Model):
    user = User.ForeignKey(User, on_delete=User.CASCADE)
```
```

## Contributing

* Please raise an issue/feature and name your branch 'feature-n' or 'issue-n', where 'n' is the issue number.
* If you test this code with a Python version not listed above and all is well, please fork and update the README to
  include the Python version you used :)

## Additional Notes

* This project is maintained by Gobierno de Monterrey.
* The project's homepage is [here](https://github.com/gobiernodigitalmonterrey/gdmty-django-users) and issues can be
  reported [here](https://github.com/gobiernodigitalmonterrey/gdmty-django-users/issues).