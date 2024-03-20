from rest_framework import viewsets
import os
import zipfile
from django.http import Http404, HttpResponse
from django.shortcuts import get_list_or_404
from core import settings
import io


from .serializers import (
    VehicleSerializer,
    BrandSerializer,
    SaleSerializer,
    RentSerializer,
)
from .models import BaseVehicle, Brand, VehicleSale, VehicleRent
from vehicle import filters
from utils.request import request_user


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class VehicleSaleViewSet(viewsets.ModelViewSet):
    queryset = VehicleSale.objects.all()
    serializer_class = SaleSerializer
    filterset_class = filters.VehicleSaleFilter

    def get_object(self):
        user = request_user(self.request)
        if user is not None:
            return user.organization

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(vehicle__company=self.get_object()).exclude(
            vehicle__removed_at__isnull=False
        )
        return queryset


class VehicleRentViewSet(viewsets.ModelViewSet):
    queryset = VehicleRent.objects.all()
    serializer_class = RentSerializer
    filterset_class = filters.VehicleRentFilter

    def get_object(self):
        user = request_user(self.request)
        if user is not None:
            return user.organization

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(vehicle__company=self.get_object()).exclude(
            vehicle__removed_at__isnull=False
        )
        return queryset


class DownloadDocumentsViewSet(viewsets.GenericViewSet):
    queryset = BaseVehicle.objects.all()
    serializer_class = VehicleSerializer
    lookup_field = "pk"

    def get_serializer(self, *args, **kwargs):
        kwargs["fields"] = ["id", "documents"]
        return super().get_serializer(*args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset().exclude(removed_at__isnull=False)
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
