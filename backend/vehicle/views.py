from rest_framework import viewsets, generics
import os
import zipfile
from django.http import Http404, HttpResponse
from django.shortcuts import get_list_or_404
import io

from .serializers import VehicleSerializer, BrandSerializer
from .models import BaseVehicle, Brand
from vehicle import filters


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = BaseVehicle.objects.all()
    serializer_class = VehicleSerializer
    filterset_class = filters.VehicleFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.exclude(removed__isnull=False)
        return queryset

    def get_serializer(self, *args, **kwargs):
        kwargs['fields'] = [
            "id",
            "title",
            "model",
            "brand",
            "overview",
            "model_year",
            "number_plate",
            "fuel_type",
            "seating_capacity",
            "mileage",
            "accessories",
            "images",
            "documents",
            "company",
            "is_available",
        ]
    
class DownloadDocumentsViewSet(viewsets.GenericViewSet):
    queryset = BaseVehicle.objects.all()
    serializer_class = VehicleSerializer
    lookup_field = "pk"

    def get_serializer(self, *args, **kwargs):
        kwargs['fields'] = ["id", "documents"]
        return super().get_serializer(*args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset().exclude(removed__isnull=False)
        return queryset
    
    def get(self, request, *args, **kwargs):
        doc_id = request.GET.getlist("doc_id", [])
        files = []
        if doc_id:
            queryset = get_list_or_404(
                self.get_queryset(), documents__in=doc_id, removed__isnull=True
            )
        else:
            queryset = self.get_queryset()

        if queryset:
            for vehicle in queryset:
                file_format = os.path.join(settings.MEDIA_ROOT, str(vehicle.documents))
                files.append(file_format)

            zip_subdir = "%s(%s)" % (vehicle.vehicle, vehicle.vehicle.model_year)
            zip_filename = "%s.zip" % zip_subdir

            s = io.BytesIO()
            zf = zipfile.ZipFile(s, "w")

            for fpath in files:
                fdir, fname = os.path.split(fpath)
                zip_path = os.path.join(zip_subdir, fname)

                zf.write(fpath, zip_path)
            zf.close()

            response = HttpResponse(s.getvalue(), content_type="application/zip")
            response["Content-Disposition"] = "attachment; filename=%s" % zip_filename

            return response
        raise Http404