from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from utils.validators import RegexValidator
from user.manager import UserManager, MasterUserManager, ClientUserManager
from organization.models import Organization


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(
        _("Phone No."), max_length=15, validators=[RegexValidator.phone_val]
    )
    is_client = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    # ForeignKey Relation
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, null=True, blank=True
    )

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    objects = UserManager()

    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"


class MasterUser(User):
    objects = MasterUserManager()

    class Meta:
        proxy = True
        db_table = "master_user"
        verbose_name = "Master User"
        verbose_name_plural = "Master Users"

    def save(self, *args, **kwargs):
        self.is_staff = True
        self.is_superuser = True
        self.is_client = False
        super().save(*args, **kwargs)


class ClientUser(User):
    objects = ClientUserManager()

    class Meta:
        proxy = True
        db_table = "client_user"
        verbose_name = "Client User"
        verbose_name_plural = "Client Users"

    def save(self, *args, **kwargs):
        self.is_staff = False
        self.is_superuser = False
        self.is_client = True
        super().save(*args, **kwargs)
