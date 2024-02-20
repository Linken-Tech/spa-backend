# get a serializer here for feedback
"""
can refer this document
https://www.django-rest-framework.org/tutorial/1-serialization/
"""

from rest_framework import serializers
from feedback.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"
