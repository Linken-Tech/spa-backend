from django.apps import AppConfig
from django.db.models.signals import post_migrate


def create_default_value(sender, **kwargs):
    from django.contrib.auth.models import User

    try:
        User.objects.get(email="admin@mail.com")
    except User.DoesNotExist:
        User.objects.create_superuser(
            email="admin@mail.com",
            username="admin",
            password="admin",
        )


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user"

    def ready(self):
        # import accounts.signals

        post_migrate.connect(create_default_value, sender=self)
