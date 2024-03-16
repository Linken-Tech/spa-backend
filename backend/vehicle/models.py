from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.contenttypes import fields
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from file.models import Image, Document
from utils.choices import FuelType


# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(_("Brand Name"), max_length=255)
    created_at = models.DateTimeField(_("Created At"), default=timezone.now)
    modified_at = models.DateTimeField(_("Modified At"), auto_now=True)
    removed_at = models.DateTimeField(_("Removed At"), null=True, blank=True)

    class Meta:
        verbose_name = _("Vehicle Brand")
        verbose_name_plural = _("Vehicle Brands")

    def __str__(self) -> str:
        return self.brand_name


class Model(models.Model):
    model_name = models.CharField(_("Model Name"), max_length=255)
    created_at = models.DateTimeField(_("Created At"), default=timezone.now)
    modified_at = models.DateTimeField(_("Modified At"), auto_now=True)
    removed_at = models.DateTimeField(_("Removed At"), null=True, blank=True)

    class Meta:
        verbose_name = _("Vehicle Model")
        verbose_name_plural = _("Vehicle Models")

    def __str__(self) -> str:
        return self.model_name


class BaseVehicle(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    model = models.ForeignKey("vehicle.Model", on_delete=models.CASCADE)
    brand = models.ForeignKey("vehicle.Brand", on_delete=models.CASCADE)
    overview = models.CharField(_("Overview"), max_length=255)
    model_year = models.IntegerField(_("Model Year"), default=None)
    number_plate = models.CharField(_("Number Plate"), max_length=10)
    fuel_type = models.CharField(
        _("Fuel Type"), max_length=50, choices=FuelType.choices
    )
    seating_capacity = models.IntegerField(_("Seating Capacity"))
    mileage = models.IntegerField(_("Mileage"))
    # accessories = ArrayField(_('Accessories'), models.CharField(max_length=100), max_length=255, default=None)
    accessories = ArrayField(
        models.CharField(max_length=100), size=10, max_length=255, default=None
    )
    images = fields.GenericRelation(Image)
    documents = fields.GenericRelation(Document)
    company = models.ForeignKey("organization.Organization", on_delete=models.CASCADE)
    is_available = models.BooleanField(_("Is Available"), default=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified At"), auto_now=True)

    class Meta:
        verbose_name = _("Vehicle")
        verbose_name_plural = _("Vehicle")


class VehicleRent(models.Model):
    price_per_day = models.DecimalField(
        _("Price Per Day"), max_digits=65, decimal_places=2
    )
    price_per_month = models.DecimalField(
        _("Price Per Month"), max_digits=65, decimal_places=2
    )
    is_rent = models.BooleanField(_("Is Rent"), default=False)
    vehicle = models.ForeignKey("vehicle.BaseVehicle", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Vehicle Rent")
        verbose_name_plural = _("Vehicle Rent")

    def __str__(self) -> str:
        return f"{self.title} - {self.brand} - {self.model}"


class VehicleSale(models.Model):
    cost_price = models.DecimalField(_("Cost Price"), max_digits=65, decimal_places=2)
    sale_price = models.DecimalField(_("Sale Price"), max_digits=65, decimal_places=2)
    vehicle = models.ForeignKey("vehicle.BaseVehicle", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Vehicle Sale")
        verbose_name_plural = _("Vehicle Sale")

    def __str__(self) -> str:
        return f"{self.title} - {self.brand} - {self.model}"