from rest_framework import serializers
from vehicle.models import Brand, VehicleSale, VehicleRent, Model, BaseVehicle
from file.serializers import ImageSerializer, DocsSerializer
from organization.serializers import OrganizationSerializer


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["brand_name"]


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ["model_name"]


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleSale
        fields = ["cost_price", "sale_price"]


class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleRent
        fields = ["price_per_day", "price_per_month", "is_rent"]


class VehicleSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    model = ModelSerializer()
    accessories = serializers.ListField(write_only=True)
    images = serializers.ListField(write_only=True, required=False)
    documents = serializers.ListField(write_only=True, required=False)
    company = OrganizationSerializer()
    sale_or_rent_vehicle = serializers.SerializerMethodField(
        method_name="get_sale_or_rent_vehicle"
    )
    delete_images = serializers.ListField(write_only=True, required=False)
    delete_documents = serializers.ListField(write_only=True, required=False)

    class Meta:
        model = BaseVehicle
        fields = [
            "id"
            "title",
            "model",
            "brand",
            "overview",
            "model_year",
            "number_plate",
            "fuel_type",
            "seating_capacity",
            "mileage",
            "accessories",
            "images",
            "documents",
            "company",
            "is_available",
            "sale_or_rent_vehicle",
            "delete_images",
            "delete_documents",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["brand"] = BrandSerializer(instance.brand).data
        representation["model"] = ModelSerializer(instance.model).data
        representation["accessories"] = instance.accessories
        representation["images"] = ImageSerializer(
            instance.vehicle_image.all(), many=True
        ).data
        representation["documents"] = DocsSerializer(
            instance.documents.all(), many=True
        ).data
        representation["company"] = OrganizationSerializer(instance.company).data
        return representation

    def get_sale_or_rent_vehicle(self, obj):
        exist_sale = VehicleSale.objects.filter(vehicle=obj)
        exist_rent = VehicleRent.objects.filter(vehicle=obj)
        if exist_sale.exists():
            return SaleSerializer(instance=exist_sale).data
        if exist_rent.exists():
            return RentSerializer(instance=exist_rent).data
