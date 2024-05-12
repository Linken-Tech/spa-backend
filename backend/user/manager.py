from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        from user.models import User

        if not username:
            raise ValueError("The given username must be set")

        username = User.normalize_username(username)
        auth = User(username=username, **extra_fields)
        auth.password = make_password(password)
        auth.save(using=self._db)
        return auth

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, password, **extra_fields)


class MasterUserManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_staff=True, is_superuser=True)


class ClientUserManager(UserManager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(is_staff=False, is_superuser=False, is_client=True)
        )
