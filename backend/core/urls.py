"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.conf import settings
from django.conf.urls.static import static

from user.views import AuthViewSet, UserViewSet, UserLogin
from feedback.views import FeedbackViewSet
from vehicle.views import (
    BrandViewSet,
    VehicleSaleViewSet,
    VehicleRentViewSet,
    DownloadDocumentsViewSet,
    ModelViewSet,
)
from organization.views import OrganizationViewSet
from utils.views import HealthCheckView, ErrorCheckView

schema_view_v1 = get_schema_view(
    openapi.Info(
        title="SPA Project API",
        default_version="v1",
        description="Spa Project V1 API Endpoint",
        license=openapi.License(name="Linken Tech License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

schema_view_v2 = get_schema_view(
    openapi.Info(
        title="SPA Project API",
        default_version="v2",
        description="Spa Project V2 API Endpoint",
        license=openapi.License(name="Linken Tech License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# v2 api
router_v2 = routers.SimpleRouter()
router_v2.register(r"auth", AuthViewSet, basename="auth")
router_v2.register(r"user", UserViewSet, basename="user")
router_v2.register(r"feedback", FeedbackViewSet, basename="feedback")
router_v2.register(r"brand", BrandViewSet, basename="brand")
router_v2.register(r"vehicle-model", ModelViewSet, basename="model")
router_v2.register(r"vehicle-sale", VehicleSaleViewSet, basename="vehicle-sale")
router_v2.register(r"vehicle-rent", VehicleRentViewSet, basename="vehicle-rent")
router_v2.register(r"download-docs", DownloadDocumentsViewSet, basename="download-docs")
router_v2.register(r"organization", OrganizationViewSet, basename="organization")

# v1 api
router_v1 = routers.SimpleRouter()
router_v1.register(r"feedback", FeedbackViewSet, basename="feedback")

urlpatterns = [
    path("v2/health-check/", HealthCheckView.as_view(), name="health-check"),
    path("v2/error-check/", ErrorCheckView.as_view(), name="error-check"),
    path("v2/auth/login", UserLogin.as_view(), name="login"),
    path('auth/token/refresh/',
        TokenRefreshView.as_view(),name='api-token-refresh'),
    path('auth/token/verify/',
        TokenVerifyView.as_view(), name='api-token-verify'),
    path("v2/", include(router_v2.urls)),
    re_path(
        r"^v2-swagger(?P<format>\.json|\.yaml)$",
        schema_view_v2.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^v2-swagger/$",
        schema_view_v2.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^v2-redoc/$",
        schema_view_v2.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    # v1 api
    path("health-check/", HealthCheckView.as_view(), name="health-check"),
    path("error-check/", ErrorCheckView.as_view(), name="error-check"),
    path("", include(router_v1.urls)),
    path("vehicle/", include("vehicle.urls")),
    path("admin/", admin.site.urls),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view_v1.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view_v1.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$",
        schema_view_v1.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
