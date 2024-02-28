from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from utils.validators import RegexValidator
from user.manager import UserManager


class UserAuth(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    is_staff = models.BooleanField(_("Is Staff"), default=False)
    is_admin = models.BooleanField(_("Is Admin"), default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["password"]

    objects = UserManager()

    class Meta:
        verbose_name = _("User Auth")
        verbose_name_plural = _("User Auth")

    def __str__(self) -> str:
        return self.username


class User(models.Model):
    user_auth = models.OneToOneField("UserAuth", on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(
        _("Phone No."), max_length=15, validators=[RegexValidator.phone_val]
    )
    organization = models.ForeignKey(
        "organization.Organization", on_delete=models.CASCADE
    )
    is_active = models.BooleanField(_("Is Active"), default=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified At"), auto_now=True)

    objects = models.Manager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self) -> str:
        return self.fullname
