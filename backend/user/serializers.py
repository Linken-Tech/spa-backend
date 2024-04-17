from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.hashers import make_password

from user.models import User, UserAuth
from organization.serializers import OrganizationSerializer


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAuth
        fields = ["username", "password"]

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        created = super().create(validated_data)
        created.password = make_password(password)
        created.save()
        return created


class UserSerializer(serializers.ModelSerializer):
    user_auth = serializers.SerializerMethodField(
        method_name="get_auth", read_only=True
    )
    organization = OrganizationSerializer()

    class Meta:
        model = User
        fields = [
            "user_auth",
            "fullname",
            "email",
            "phone",
            "organization",
            "is_active",
        ]

    def get_auth(self, obj):
        return obj.user_auth.username


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        super().validate(attrs)
        if not UserAuth.objects.filter(username=attrs["username"]).exists():
            raise PermissionDenied()
        data = super().validate(attrs)
        return data
