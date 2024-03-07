from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class RegexValidator:
    phone_val = RegexValidator(
        regex=r"^\+?1?\d{7,15}$", message=_("Only 7 - 15 digits are allowed.")
    )
