# from io import StringIO
from vehicle.models import Vehicle, VehicleBrand, VehicleDocument
from rest_framework import generics
from vehicle import serializers as vehicle_srlz
from django.utils import timezone
import os
import zipfile
from django.http import Http404, HttpResponse
from core import settings
import io
from django.shortcuts import get_list_or_404
from vehicle import filters


# Vehicle Brand Here
class BrandList(generics.ListCreateAPIView):
    """
    Create New Brand
    View All Brand in a List
    """

    queryset = VehicleBrand.objects.exclude(removed__isnull=False)
    serializer_class = vehicle_srlz.VehicleBrandSerializer


class BrandDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    View Brand Details
    Update Brand Details
    Delete Brand
    """

    queryset = VehicleBrand.objects.all()
    serializer_class = vehicle_srlz.VehicleBrandSerializer

    def perform_destroy(self, instance):
        instance.removed = timezone.now()
        return instance.save()


# Vehicle Here
class VehicleList(generics.ListCreateAPIView):
    """
    Create New Car
    View All Car in a List
    """

    queryset = Vehicle.objects.exclude(removed__isnull=False)
    serializer_class = vehicle_srlz.VehicleSerializer
    filterset_class = filters.VehicleFilter


class VehicleDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    View Car Details
    Update Car Details
    Delete Car
    """

    queryset = Vehicle.objects.all()
    serializer_class = vehicle_srlz.VehicleSerializer

    def perform_destroy(self, instance):
        queryset_doc = instance.documents.filter(vehicle_id=instance)
        queryset_images = instance.vehicle_image.filter(vehicle_id=instance)
        queryset_doc.update(removed=timezone.now())
        queryset_images.update(removed=timezone.now())
        instance.removed = timezone.now()
        return instance.save()


class DownloadVehicleDocuments(generics.GenericAPIView):
    """
    Download Vehicle Document
    """

    queryset = VehicleDocument.objects.all()
    serializer_class = vehicle_srlz.DownloadVehicleDocumentSerializer
    lookup_field = "vehicle"

    def get_queryset(self):
        queryset = (
            super()
            .get_queryset()
            .filter(vehicle=self.kwargs.get("vehicle"))
            .exclude(removed__isnull=False)
        )
        return queryset

    def get(self, request, *args, **kwargs):
        doc_id = request.GET.getlist("doc_id", [])
        files = []
        if doc_id:
            queryset = get_list_or_404(
                VehicleDocument, pk__in=doc_id, removed__isnull=True
            )
        else:
            queryset = self.get_queryset()

        if queryset:
            for vehicle in queryset:
                file_format = os.path.join(settings.MEDIA_ROOT, str(vehicle.document))
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
