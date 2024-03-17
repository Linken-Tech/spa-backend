from rest_framework import serializers
from organization.models import Organization, OrganizationContact


class OrganizationContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationContact
        fields = ["contact_name", "phone", "position"]


class OrganizationSerializer(serializers.ModelSerializer):
    profile_pic = serializers.ImageField(required=False)
    contact_details = OrganizationContactSerializer(
        source="organizationcontact_set", many=True
    )

    class Meta:
        model = Organization
        fields = ["company_name", "email", "address", "profile_pic"]
