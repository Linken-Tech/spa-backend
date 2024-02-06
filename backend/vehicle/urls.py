from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from vehicle import views

urlpatterns = [
    # Add and View Brand list
    path('brand/', views.BrandList.as_view()),
    # View, Update and Delete Brand details with ID
    path('brand/<pk>/', views.BrandDetails.as_view()),
    # Add and View Car list
    path('vehicle/', views.VehicleList.as_view()),
    # View, Update, Delete Car Details
    path('vehicle/<pk>/', views.VehicleDetails.as_view()),
    # Download Vehicle Documents
    path('vehicle-document/<int:vehicle>/download/', views.DownloadVehicleDocuments.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)