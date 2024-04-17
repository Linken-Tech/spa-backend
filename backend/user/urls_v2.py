from rest_framework import routers

from user.views import AuthViewSet, UserViewSet

router = routers.SimpleRouter()
router.register(r"auth", AuthViewSet, basename="auth")
router.register(r"user", UserViewSet, basename="user")

urlpatterns = router.urls
