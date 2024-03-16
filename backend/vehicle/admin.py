# from django.contrib import admin
# from vehicle.models_v2 import VehicleSale, VehicleRent, Brand, BaseVehicle
# from file.admin import ImageInlineAdmin, DocumentInlineAdmin


# # Custom Admin
# # class VehicleRentAdmin(admin.ModelAdmin):
# #     model = VehicleRent
# #     list_display = ("title", "brand", "price_per_day", "price_per_month", "is_rent")
# #     list_filter = ["brand"]
# #     ordering = ("brand",)
# #     search_fields = ["title", "brand__brand_name"]


# # class VehicleSaleAdmin(admin.ModelAdmin):
# #     model = VehicleSale
# #     list_display = ("title", "brand", "sale_price", "cost_price", "is_available")
# #     list_filter = ["brand"]
# #     ordering = ("brand",)
# #     search_fields = ["title", "brand__brand_name"]

# class ImageIncline(ImageInlineAdmin):
#     verbose_name = "Image"
#     verbose_name_plural = "Image"

# class DocsIncline(DocumentInlineAdmin):
#     verbose_name = "Document"
#     verbose_name_plural = "Document"

# class VehicleSaleIncline(admin.TabularInline):
#     model = VehicleSale
#     fields = ("cost_price", "sale_price",)
#     extra = 0

# class VehicleRentIncline(admin.TabularInline):
#     model = VehicleRent
#     fields = ("price_per_day", "price_per_month", "is_rent",)
#     extra = 0

# @admin.register(BaseVehicle)
# class VehicleAdmin(admin.ModelAdmin):
#     model = BaseVehicle
#     list_display = ("title", "brand", "sale_price", "cost_price", "is_available")
#     list_filter = ["brand"]
#     ordering = ("brand",)
#     search_fields = ["title", "brand__brand_name"]
#     inlines = [VehicleSaleIncline, VehicleRentIncline, ImageIncline, DocsIncline]
#     # fieldsets = [
#     #     ("VEHICLE INFORMATION", {
#     #         "fields": ("title", "model", "brand", "overview", "model_year", "number_plate", "fuel_type", "seating_capacity", "mileage", "accessories", "is_available", "created_at", "modified_at", )
#     #     },
#     #     {
#     #         "SALE", {
#     #             "fields": ("cost_price", "sale_price",)
#     #         }
#     #     },
#     #     {
#     #         "RENT", {
#     #             "fields": ("price_per_day", "price_per_month", "is_rent",)
#     #         }
#     #     }
#     #     )
#     # ]

# # Register your models here.
# # admin.site.register(VehicleRent, VehicleRentAdmin)
# # admin.site.register(VehicleSale, VehicleSaleAdmin)
# admin.site.register(Brand)
