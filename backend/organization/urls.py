from rest_framework import routers

from organization.views import OrganizationViewSet

router = routers.SimpleRouter()
router.register(r"organization", OrganizationViewSet, basename="organization")

urlpatterns = router.urls
