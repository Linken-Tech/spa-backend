from rest_framework import viewsets

from .serializers import VehicleSerializer, BrandSerializer
from .models import BaseVehicle, Brand
from vehicle import filters


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = BaseVehicle.objects.all().exclude(removed__isnull=False)
    serializer_class = VehicleSerializer
    filterset_class = filters.VehicleFilter

    # def delete(self, instance):
        # queryset_doc = instance.documents.filter(vehicle_id=instance)
        # queryset_images = instance.vehicle_image.filter(vehicle_id=instance)
        # queryset_doc.update(removed=timezone.now())
        # queryset_images.update(removed=timezone.now())
        # instance.removed = timezone.now()
        # return instance.save()
    
# class DownloadVehicleDocuments():
#     queryset = 


