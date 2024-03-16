from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group as OriginalGroup
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from .managers import CustomUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField

username_validator = UnicodeUsernameValidator()


class User(AbstractUser):
    history = AuditlogHistoryField(pk_indexable=False)
    email = models.EmailField(unique=True)
    safe_delete = models.BooleanField(default=False)
    username = models.CharField(
        _("username"),
        max_length=150,
        primary_key=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ solamente."),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email_verificado = models.BooleanField(default=False)   

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    @property
    def id(self):
        return self.pk

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email.split('@')[0]
        super(User, self).save(*args, **kwargs)

    @staticmethod
    @receiver(pre_delete, sender='gdmty_django_users.User')
    def safe_delete_user(sender, instance, **kwargs):
        instance.safe_delete = True
        instance.save()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Group(OriginalGroup):
    class Meta:
        proxy = True
        verbose_name = "Group"
        verbose_name_plural = "Groups"


auditlog.register(User)
auditlog.register(Group)
