from rest_framework import viewsets


from user.models import UserAuth, User
from user.serializers import AuthSerializer, UserSerializer


class AuthViewSet(viewsets.ModelViewSet):
    queryset = UserAuth.objects.all()
    serializer_class = AuthSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
