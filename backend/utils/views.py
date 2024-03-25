from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class HealthCheckView(generics.GenericAPIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK, data="Deploy from cicds")


class ErrorCheckView(generics.GenericAPIView):
    def get(self, request):
        data = 1 / 0
        return Response(status=status.HTTP_200_OK, data=data)
