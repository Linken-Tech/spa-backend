from django.shortcuts import render

# Create your views here.

# work on the crud logic and views
"""
can refer this documentation
https://www.django-rest-framework.org/tutorial/3-class-based-views/

"""

from django.shortcuts import render
from feedback.models import Feedback
from rest_framework import generics
from rest_framework.views import APIView
from feedback.serializers import FeedbackSerializer
from rest_framework.response import Response

# Feedback
class Feedback(APIView):
    def get(self, request, format=None):
        feedback = feedback.objects.all()
        serializer = FeedbackSerializer(feedback, many=True)
        return Response(serializer.data)
