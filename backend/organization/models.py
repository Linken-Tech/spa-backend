from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes import fields

from file.models import Image
from utils.validators import RegexValidator


# Create your models here.
class Organization(models.Model):
    company_name = models.CharField(_("Company Name"), max_length=200, unique=True)
    email = models.EmailField(_("Email"), max_length=200)
    address = models.TextField(_("Address"))
    profile_pic = fields.GenericRelation(Image)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified At"), auto_now=True)

    class Meta:
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")

    def __str__(self) -> str:
        return self.company_name


class OrganizationContact(models.Model):
    contact_name = models.CharField(_("Contact Name"), max_length=255)
    phone = models.CharField(
        _("Phone No."), max_length=15, validators=[RegexValidator.phone_val]
    )
    position = models.CharField(_("Position"), max_length=100)
    company = models.ForeignKey("organization.Organization", on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified At"), auto_now=True)

    class Meta:
        verbose_name = _("Organization Contact")
        verbose_name_plural = _("Organization Contacts")

    def __str__(self) -> str:
        return self.company.company_name
