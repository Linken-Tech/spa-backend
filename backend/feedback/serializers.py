# get a serializer here for feedback
"""
can refer this document
https://www.django-rest-framework.org/tutorial/1-serialization/
"""

from pyexpat import model
from pkg_resources import require
from rest_framework import serializers
import feedback
from feedback.models import *
    
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
