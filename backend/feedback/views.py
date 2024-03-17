# work on the crud logic and views
"""
can refer this documentation
https://www.django-rest-framework.org/tutorial/3-class-based-views/

"""

from rest_framework import viewsets

from feedback.serializers import FeedbackSerializer
from .models import Feedback


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
