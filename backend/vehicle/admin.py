from django.contrib import admin
from vehicle.models import *

# Custom Admin
class VehicleAdmin(admin.ModelAdmin):
    model = Vehicle
    list_display = (
        "vehicle",
        "vehicle_brand",
        "price_per_day",
        "price_per_month",
        "price_of_cost",
        "price_of_sale",
    )
    list_filter = ["vehicle_brand"]
    ordering =("vehicle_brand",)
    search_fields = ["vehicle","vehicle_brand__brand_name"]


# Register your models here.
admin.site.register(Vehicle,VehicleAdmin)
admin.site.register(VehicleBrand)
admin.site.register(VehicleDocument)
admin.site.register(VehicleImage)