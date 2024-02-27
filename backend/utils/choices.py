from django.db import models


class FuelType(models.TextChoices):
    PETROL = "PETROL", ("Petrol")
    HYBRID = "HYBRID", ("Hybrid")
    EV = "EV", ("EV")
