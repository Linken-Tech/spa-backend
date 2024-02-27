from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.validators import RegexValidator


# Create your models here.
class Feedback(models.Model):
    title = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=200)
    customer_phone = models.CharField(
        _("Phone No."), max_length=15, validators=[RegexValidator.phone_val]
    )
    description = models.TextField()
    organization = models.ForeignKey(
        "organization.Organization", on_delete=models.CASCADE
    )
    is_solved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
