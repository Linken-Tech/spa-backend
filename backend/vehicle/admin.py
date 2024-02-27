from django.contrib import admin
from vehicle.models import VehicleSale, VehicleRent, VehicleBrand


# Custom Admin
class VehicleRentAdmin(admin.ModelAdmin):
    model = VehicleRent
    list_display = ("title", "brand", "price_per_day", "price_per_month")
    list_filter = ["brand"]
    ordering = ("brand",)
    search_fields = ["title", "brand__brand_name"]


class VehicleSaleAdmin(admin.ModelAdmin):
    model = VehicleSale
    list_display = ("title", "brand", "sale_price", "cost_price")
    list_filter = ["brand"]
    ordering = ("brand",)
    search_fields = ["title", "brand__brand_name"]


# Register your models here.
admin.site.register(VehicleRent, VehicleRentAdmin)
admin.site.register(VehicleSale, VehicleSaleAdmin)
admin.site.register(VehicleBrand)
