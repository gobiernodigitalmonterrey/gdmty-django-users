# gdmty-django-users

This is a custom Django Rest Framework authentication backend project named `gdmty-django-users`. It is designed to
authenticate users in the Administration panel based on email and password, with reCaptcha token verification.

The project is built with Python and Django, and it requires Python version 3.10 or later and Django version 4.2 or
later. It also depends on other packages such as `djangorestframework` and `auditlog`.

The project is maintained by Gobierno de Monterrey and the current version is 24.3.0. You can find more about the
project on its [homepage](https://github.com/gobiernodigital/gdmty-django-users) or report issues on
the [bug tracker](https://github.com/gobiernodigital/gdmty-django-users/issues).

## Features

- Email and password-based authentication for users in the Administration panel.
- reCaptcha token verification for added security.
- Compatibility with Python 3.10 and later, and Django 4.2 and later.

## Requirements

* Python 3
* Django 4
* Django Rest Framework 3
* Firebase Admin SDK

## Installation

```bash
$ pip install gdmty-django-users
```

## Configuration

Add the application to your project's `INSTALLED_APPS` in `settings.py`.

```python
INSTALLED_APPS = [
    # ...
    'gdmty_django_users',
    ...
]
# TODO PONER LAS VARIABLES QUE SE NECESITAN PARA QUE FUNCIONE
```
In your code models.py, add the following line to the top of the file:
    
    ```python 
    from gdmty_django_users.models import User

    class MyModel(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
    ```

## Contributing

* Please raise an issue/feature and name your branch 'feature-n' or 'issue-n', where 'n' is the issue number.
* If you test this code with a Python version not listed above and all is well, please fork and update the README to
  include the Python version you used :)

## Additional Notes

* This project is maintained by Gobierno de Monterrey.
* The project's homepage is [here](https://github.com/gobiernodigital/gdmty-django-users) and issues can be
  reported [here](https://github.com/gobiernodigital/gdmty-django-users/issues).