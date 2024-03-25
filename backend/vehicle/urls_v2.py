from rest_framework import routers

from vehicle.views import (
    BrandViewSet,
    ModelViewSet,
    VehicleSaleViewSet,
    VehicleRentViewSet,
    DownloadDocumentsViewSet,
)

router = routers.SimpleRouter()
router.register(r"brand", BrandViewSet, basename="brand")
router.register(r"vehicle-model", ModelViewSet, basename="model")
router.register(r"vehicle-sale", VehicleSaleViewSet, basename="vehicle-sale")
router.register(r"vehicle-rent", VehicleRentViewSet, basename="vehicle-rent")
router.register(r"download-docs", DownloadDocumentsViewSet, basename="download-docs")

urlpatterns = router.urls
