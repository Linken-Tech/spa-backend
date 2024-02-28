from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.validators import RegexValidator


# Create your models here.
class Feedback(models.Model):
    title = models.CharField(_("Title"), max_length=50, null=True)
    customer_name = models.CharField(
        _("Customer Name"), max_length=100, default="anonymous"
    )
    customer_email = models.EmailField(_("Customer Email"), max_length=200, null=True)
    customer_phone = models.CharField(
        _("Phone No."), max_length=15, validators=[RegexValidator.phone_val], null=True
    )
    description = models.TextField(_("Description"), null=True)
    organization = models.ForeignKey(
        "organization.Organization", on_delete=models.CASCADE, null=True
    )
    is_solved = models.BooleanField(_("Is Solved"), default=False)
    created_at = models.DateTimeField(_("Created At"), default=timezone.now)
    modified_at = models.DateTimeField(_("Modified At"), auto_now=True)

    def __str__(self):
        return self.title
