from rest_framework import viewsets
from .serializers_v1 import VehicleSerializer
from .models import BaseVehicle


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = BaseVehicle.objects.all()
    serializer_class = VehicleSerializer
