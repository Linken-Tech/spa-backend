from rest_framework import serializers
from user.models import User, UserAuth
from organization.serializers import OrganizationSerializer


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAuth
        fields = ["username", "password"]


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
