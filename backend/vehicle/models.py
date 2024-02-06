from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
def vehicle_image_upload_path(instance, filename):
    return '{}/{}/image/{}'.format(instance.vehicle.vehicle_brand.brand_name,
                                   instance.vehicle.vehicle,
                                   filename)

def vehicle_document_upload_path(instance, filename):
    return '{}/{}/document/{}'.format(instance.vehicle.vehicle_brand.brand_name,
                                      instance.vehicle.vehicle,
                                      filename)

class VehicleBrand(models.Model):
    brand_name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    removed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.brand_name

sales_type = [
    ('Sales','Sales'),
    ('Rent','Rent'),
]

# fuel_type = [
    # ('Petrol','Petrol'),
    # ('Hybrid','Hybrid'),
    # ('EV','EV'),
# ]
# class VehicleRent(models.Model):
#     price_per_day = models.DecimalField(default=0, max_digits=65, decimal_places=2)
#     price_per_month = models.DecimalField(default=0, max_digits=65, decimal_places=2)
#     is_active = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

class Vehicle(models.Model):
    vehicle = models.CharField(max_length=255)
    vehicle_brand = models.ForeignKey(VehicleBrand, on_delete=models.CASCADE)
    vehicle_overview = models.CharField(max_length=255)  
    number_plate = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    # vehicle_rent = models.OneToOneField(VehicleRent, on_delete=models.CASCADE, null=True)
    price_per_day = models.DecimalField(max_digits=65, decimal_places=2, null=True, blank=True)
    price_per_month = models.DecimalField(max_digits=65, decimal_places=2, null=True, blank=True)
    price_of_cost = models.DecimalField(max_digits=65,decimal_places=2, null=True, blank=True)
    price_of_sale = models.DecimalField(max_digits=65,decimal_places=2, null=True, blank=True)
    fuel_type = models.CharField(max_length=50)
    model_year = models.IntegerField(default=None)
    seating_capacity = models.IntegerField(default=None)
    mileage = models.IntegerField(default=None)
    accessories = ArrayField(models.CharField(max_length=100), size=10, max_length=255, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    removed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.vehicle

class VehicleDocument(models.Model):
    document = models.FileField(null=True, upload_to=vehicle_document_upload_path)
    vehicle = models.ForeignKey(Vehicle, related_name='documents', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    removed = models.DateTimeField(null=True, blank=True)

class VehicleImage(models.Model):   
    vehicle_image = models.ImageField(upload_to=vehicle_image_upload_path)
    vehicle = models.ForeignKey(Vehicle, related_name='vehicle_image', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    removed = models.DateTimeField(null=True, blank=True)