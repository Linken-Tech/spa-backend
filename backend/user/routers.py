from rest_framework import routers
from user.views import MenuViewSet


router = routers.SimpleRouter()
router.register(r'menu', MenuViewSet, basename='menu')