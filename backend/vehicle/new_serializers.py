from rest_framework import serializers
from vehicle.models import VehicleBrand, VehicleSale, VehicleRent, VehicleModel, Vehicle
from file.serializers import ImageSerializer, DocsSerializer

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleBrand
        fields = ["brand_name"]

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
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
    accessories = serializers.ListField(write_only=True)
    images = serializers.ListField(write_only=True, required=False)
    documents = serializers.ListField(write_only=True, required=False)
    sale = SaleSerializer()
    rent = RentSerializer()
    delete_images = serializers.ListField(write_only=True, required=False)
    delete_documents = serializers.ListField(write_only=True, required=False)
    class Meta:
        model = Vehicle
        fields = ["title", "model", "brand", "overview", "model_year", "number_plate", "fuel_type", "seating_capacity", "mileage", "accessories", "images", "documents", "is_available", "sale", "rent", "delete_images", "delete_documents"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["brand"] = BrandSerializer(instance.brand).data
        representation["model"] = ModelSerializer(instance.model).data
        representation["accessories"] = instance.accessories
        representation["images"] = ImageSerializer(instance.vehicle_image.all(), many=True).data
        representation["documents"] = DocsSerializer(instance.documents.all(), many=True).data
        return representation
    