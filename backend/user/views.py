from rest_framework import status, viewsets, views
from rest_framework.response import Response


from user.models import UserAuth, User
from user.serializers import AuthSerializer, UserSerializer


class HealthCheckView(views.APIView):
    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK, data="Deploy from cicds")


class ErrorCheckView(views.APIView):
    def get(self, request, *args, **kwargs):
        data = 1 / 0
        return Response(status=status.HTTP_200_OK, data=data)


class AuthViewSet(viewsets.ModelViewSet):
    queryset = UserAuth.objects.all()
    serializer_class = AuthSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
