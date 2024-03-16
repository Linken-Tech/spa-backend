from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from vehicle import views_v1

urlpatterns = [
    # Add and View Brand list
    path("brand/", views_v1.BrandList.as_view()),
    # View, Update and Delete Brand details with ID
    path("brand/<pk>/", views_v1.BrandDetails.as_view()),
    # Add and View Car list
    path("vehicle/", views_v1.VehicleList.as_view()),
    # View, Update, Delete Car Details
    path("vehicle/<pk>/", views_v1.VehicleDetails.as_view()),
    # Download Vehicle Documents
    path(
        "vehicle-document/<int:vehicle>/download/",
        views_v1.DownloadVehicleDocuments.as_view(),
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
