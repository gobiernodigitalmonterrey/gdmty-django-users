from django.conf import settings
from functools import wraps
from gdmty_django_recaptcha_enterprise.decorators import requires_recaptcha_token

enabled_recaptcha = getattr(settings, 'ENABLE_RECAPTCHA', False)


def recaptcha_verify(action=None):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if enabled_recaptcha:
                return requires_recaptcha_token(action)(view_func)(request, *args, **kwargs)
            else:
                return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator