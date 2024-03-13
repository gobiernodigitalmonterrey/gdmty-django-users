from rest_framework import viewsets

from apirest.utils import verificar_token
from .models import User, Group
from django.contrib.auth.models import Permission
from .serializers import UserSerializer, GroupSerializer, PermissionSerializer
from .permissions import IsAuthenticatedAndSelfOrIsStaff, IsAuthenticatedAndObjUserOrIsStaff
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from gdmty_django_recaptcha_enterprise.recaptcha import RecaptchaEnterprise
from django.conf import settings

recaptcha = RecaptchaEnterprise(
    settings.RECAPTCHA_ENTERPRISE_PROJECT_ID,
    settings.RECAPTCHA_ENTERPRISE_SITE_KEY_VERIFY,
    settings.RECAPTCHA_ENTERPRISE_SERVICE_ACCOUNT_CREDENTIALS)


class UserViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email', 'username']

    def get_serializer_class(self):
        # TODO: poner condicionales para que solo se pueda editar el usuario logueado o si es staff pueda editar a todos
        if self.request.user.is_authenticated:
            return UserSerializer
        else:
            return Response('Unauthorized', status=401)

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        elif self.request.user.is_authenticated:
            return User.objects.filter(username=self.request.user.username)
        else:
            return Response('Unauthorized', status=401)

    @verificar_token(recaptcha, 'verify')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @verificar_token(recaptcha, 'verify')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @verificar_token(recaptcha, 'verify')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    permission_classes = [IsAuthenticatedAndSelfOrIsStaff]
    http_method_names = ['get', 'put', 'patch', 'head', 'options']


class GroupViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        # TODO: poner condicionales para que solo se pueda editar el usuario logueado o si es staff pueda editar a todos
        if self.request.user.is_authenticated:
            return GroupSerializer
        else:
            return Response('Unauthorized', status=401)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Group.objects.all()
        elif self.request.user.is_authenticated:
            return self.request.user.groups.all()
        else:
            return Response('Unauthorized', status=401)

    @verificar_token(recaptcha, 'verify')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @verificar_token(recaptcha, 'verify')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    permission_classes = [IsAuthenticatedAndSelfOrIsStaff]
    http_method_names = ['get', 'put', 'patch', 'head', 'options']


class PermissionViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        # TODO: poner condicionales para que solo se pueda editar el usuario logueado o si es staff pueda editar a todos
        if self.request.user.is_authenticated:
            return PermissionSerializer
        else:
            return Response('Unauthorized', status=401)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Permission.objects.all()
        elif self.request.user.is_authenticated:
            return self.request.user.user_permissions.all()
        else:
            return Response('Unauthorized', status=401)

    @verificar_token(recaptcha, 'verify')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @verificar_token(recaptcha, 'verify')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    permission_classes = [IsAuthenticatedAndSelfOrIsStaff]
    http_method_names = ['get', 'put', 'patch', 'head', 'options']

