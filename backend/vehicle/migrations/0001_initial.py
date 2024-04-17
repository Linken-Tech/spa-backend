# Generated by Django 4.1.2 on 2024-03-17 10:13

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import vehicle.models_v1


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("organization", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BaseVehicle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                ("overview", models.CharField(max_length=255, verbose_name="Overview")),
                (
                    "model_year",
                    models.IntegerField(default=None, verbose_name="Model Year"),
                ),
                (
                    "number_plate",
                    models.CharField(max_length=10, verbose_name="Number Plate"),
                ),
                (
                    "fuel_type",
                    models.CharField(
                        choices=[
                            ("PETROL", "Petrol"),
                            ("HYBRID", "Hybrid"),
                            ("EV", "EV"),
                        ],
                        max_length=50,
                        verbose_name="Fuel Type",
                    ),
                ),
                (
                    "seating_capacity",
                    models.IntegerField(verbose_name="Seating Capacity"),
                ),
                ("mileage", models.IntegerField(verbose_name="Mileage")),
                (
                    "accessories",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=100),
                        default=None,
                        max_length=255,
                        size=10,
                    ),
                ),
                (
                    "is_available",
                    models.BooleanField(default=True, verbose_name="Is Available"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="Modified At"),
                ),
            ],
            options={
                "verbose_name": "Vehicle",
                "verbose_name_plural": "Vehicle",
            },
        ),
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "brand_name",
                    models.CharField(max_length=255, verbose_name="Brand Name"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Created At"
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="Modified At"),
                ),
                (
                    "removed_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Removed At"
                    ),
                ),
            ],
            options={
                "verbose_name": "Vehicle Brand",
                "verbose_name_plural": "Vehicle Brands",
            },
        ),
        migrations.CreateModel(
            name="Model",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "model_name",
                    models.CharField(max_length=255, verbose_name="Model Name"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Created At"
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="Modified At"),
                ),
                (
                    "removed_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Removed At"
                    ),
                ),
            ],
            options={
                "verbose_name": "Vehicle Model",
                "verbose_name_plural": "Vehicle Models",
            },
        ),
        migrations.CreateModel(
            name="Vehicle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("vehicle", models.CharField(max_length=255)),
                ("vehicle_overview", models.CharField(max_length=255)),
                ("number_plate", models.CharField(max_length=10)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "price_per_day",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=65, null=True
                    ),
                ),
                (
                    "price_per_month",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=65, null=True
                    ),
                ),
                (
                    "price_of_cost",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=65, null=True
                    ),
                ),
                (
                    "price_of_sale",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=65, null=True
                    ),
                ),
                ("fuel_type", models.CharField(max_length=50)),
                ("model_year", models.IntegerField(default=None)),
                ("seating_capacity", models.IntegerField(default=None)),
                ("mileage", models.IntegerField(default=None)),
                (
                    "accessories",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=100),
                        default=None,
                        max_length=255,
                        size=10,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("removed", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="VehicleBrand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "brand_name",
                    models.CharField(max_length=255, verbose_name="Brand Name"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Created At"
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="Modified At"),
                ),
                (
                    "removed_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Removed At"
                    ),
                ),
            ],
            options={
                "verbose_name": "Vehicle Brand",
                "verbose_name_plural": "Vehicle Brands",
            },
        ),
        migrations.CreateModel(
            name="VehicleSale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cost_price",
                    models.DecimalField(
                        decimal_places=2, max_digits=65, verbose_name="Cost Price"
                    ),
                ),
                (
                    "sale_price",
                    models.DecimalField(
                        decimal_places=2, max_digits=65, verbose_name="Sale Price"
                    ),
                ),
                (
                    "vehicle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vehicle.basevehicle",
                    ),
                ),
            ],
            options={
                "verbose_name": "Vehicle Sale",
                "verbose_name_plural": "Vehicle Sale",
            },
        ),
        migrations.CreateModel(
            name="VehicleRent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "price_per_day",
                    models.DecimalField(
                        decimal_places=2, max_digits=65, verbose_name="Price Per Day"
                    ),
                ),
                (
                    "price_per_month",
                    models.DecimalField(
                        decimal_places=2, max_digits=65, verbose_name="Price Per Month"
                    ),
                ),
                ("is_rent", models.BooleanField(default=False, verbose_name="Is Rent")),
                (
                    "vehicle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vehicle.basevehicle",
                    ),
                ),
            ],
            options={
                "verbose_name": "Vehicle Rent",
                "verbose_name_plural": "Vehicle Rent",
            },
        ),
        migrations.CreateModel(
            name="VehicleImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "vehicle_image",
                    models.ImageField(
                        upload_to=vehicle.models_v1.vehicle_image_upload_path
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("removed", models.DateTimeField(blank=True, null=True)),
                (
                    "vehicle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vehicle_image",
                        to="vehicle.vehicle",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VehicleDocument",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "document",
                    models.FileField(
                        null=True,
                        upload_to=vehicle.models_v1.vehicle_document_upload_path,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("removed", models.DateTimeField(blank=True, null=True)),
                (
                    "vehicle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="documents",
                        to="vehicle.vehicle",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="vehicle",
            name="vehicle_brand",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="vehicle.vehiclebrand"
            ),
        ),
        migrations.AddField(
            model_name="basevehicle",
            name="brand",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="vehicle.brand"
            ),
        ),
        migrations.AddField(
            model_name="basevehicle",
            name="company",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="organization.organization",
            ),
        ),
        migrations.AddField(
            model_name="basevehicle",
            name="model",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="vehicle.model"
            ),
        ),
    ]
