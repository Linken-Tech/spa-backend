# Generated by Django 4.1.2 on 2024-02-28 02:56

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0001_initial"),
        ("vehicle", "0007_alter_vehicle_price_of_cost_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="VehicleModel",
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
        migrations.AlterModelOptions(
            name="vehiclebrand",
            options={
                "verbose_name": "Vehicle Brand",
                "verbose_name_plural": "Vehicle Brands",
            },
        ),
        migrations.RemoveField(
            model_name="vehiclebrand",
            name="created",
        ),
        migrations.RemoveField(
            model_name="vehiclebrand",
            name="removed",
        ),
        migrations.RemoveField(
            model_name="vehiclebrand",
            name="updated",
        ),
        migrations.AddField(
            model_name="vehiclebrand",
            name="created_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Created At"
            ),
        ),
        migrations.AddField(
            model_name="vehiclebrand",
            name="modified_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Modified At"),
        ),
        migrations.AddField(
            model_name="vehiclebrand",
            name="removed_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Removed At"
            ),
        ),
        migrations.AlterField(
            model_name="vehiclebrand",
            name="brand_name",
            field=models.CharField(max_length=255, verbose_name="Brand Name"),
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
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vehicle.vehiclebrand",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organization.organization",
                    ),
                ),
                (
                    "model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vehicle.vehiclemodel",
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
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vehicle.vehiclebrand",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organization.organization",
                    ),
                ),
                (
                    "model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vehicle.vehiclemodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "Vehicle Rent",
                "verbose_name_plural": "Vehicle Rent",
            },
        ),
    ]
