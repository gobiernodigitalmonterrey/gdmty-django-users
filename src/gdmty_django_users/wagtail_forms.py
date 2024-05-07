from django import forms
from django.utils.translation import gettext_lazy as _
from django.conf import settings


if 'wagtail.users' in settings.INSTALLED_APPS:
    from wagtail.users.forms import UserEditForm as WagtailUserEditForm, UserCreationForm as WagtailUserCreationForm

    class GdmtyWagtailUserEditForm(WagtailUserEditForm):
        username = forms.CharField(required=True, label=_("ID de usuario (username)"))


    class GdmtyWagtailUserCreationForm(WagtailUserCreationForm):
        username = forms.CharField(required=True, label=_("ID de usuario (username)"))
