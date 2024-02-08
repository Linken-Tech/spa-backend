from django.shortcuts import render
from rest_framework import viewsets, generics
from user.models import Menu
from user.serializers import MenuSerializer
from rest_framework.response import Response
from rest_framework import status
    
class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
        
    def get_queryset(self):
        return Menu.objects.all()
    
# @schema(None)
class HealthCheckView(generics.GenericAPIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)