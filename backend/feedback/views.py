# work on the crud logic and views
"""
can refer this documentation
https://www.django-rest-framework.org/tutorial/3-class-based-views/

"""

# from rest_framework.views import APIView
from rest_framework import viewsets
from feedback.serializers import FeedbackSerializer
# from rest_framework.response import Response
from .models import Feedback


# Feedback
# class Feedback(APIView):
#     def get(self, request, format=None):
#         feedback = Feedback.objects.all()
#         serializer = FeedbackSerializer(feedback, many=True)

#         return Response(serializer.data)
    
class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
