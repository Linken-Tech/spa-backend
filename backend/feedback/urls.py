from rest_framework import routers

from feedback.views import FeedbackViewSet

router = routers.SimpleRouter()
router.register(r"feedback", FeedbackViewSet, basename="feedback")

urlpatterns = router.urls
