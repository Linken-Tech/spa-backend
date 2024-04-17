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
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from user.urls_v2 import urlpatterns as user_urlpatterns
from feedback.urls import urlpatterns as feedback_urlpatterns
from vehicle.urls_v2 import urlpatterns as vehicle_urlpatterns
from organization.urls import urlpatterns as original_organization_urlpatterns
from utils.views import HealthCheckView, ErrorCheckView


urlpatterns = [
    path("health-check/", HealthCheckView.as_view(), name="health-check"),
    path("error-check/", ErrorCheckView.as_view(), name="error-check"),
    path("admin/", admin.site.urls),
    # Authentication
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

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

# v1 api
urlpatterns_v1 = [
    path("vehicle/", include("vehicle.urls")),
    path(
        "feedback/", include((feedback_urlpatterns, "feedback"), namespace="feedback")
    ),
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
urlpatterns_v2 = [
    path(
        r"v2/organization/",
        include(
            (original_organization_urlpatterns, "organization"),
            namespace="organization_v2",
        ),
    ),
    path(r"v2/user/", include((user_urlpatterns, "users"), namespace="users_v2")),
    path(
        r"v2/vehicle/",
        include((vehicle_urlpatterns, "vehicle"), namespace="vehicle_v2"),
    ),
    path(
        r"v2/feedback/",
        include((feedback_urlpatterns, "feedback"), namespace="feedback_v2"),
    ),
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
]

urlpatterns += urlpatterns_v1
urlpatterns += urlpatterns_v2

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
