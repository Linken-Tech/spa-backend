from django.apps import AppConfig
from django.db.models.signals import post_migrate


def create_default_value(sender, **kwargs):
    from user.models import UserAuth

    try:
        UserAuth.objects.get(username="admin")
    except UserAuth.DoesNotExist:
        UserAuth.objects.create_superuser(username="admin", password="admin")


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user"

    def ready(self):
        post_migrate.connect(create_default_value, sender=self)
