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




class VehicleSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    model = ModelSerializer()
    accessories = serializers.ListField(write_only=True)
    images = serializers.ListField(write_only=True, required=False)
    documents = serializers.ListField(write_only=True, required=False)
    company = OrganizationSerializer()
    delete_images = serializers.ListField(write_only=True, required=False)
    delete_documents = serializers.ListField(write_only=True, required=False)

    class Meta:
        model = BaseVehicle
        fields = [
            "id",
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

class SaleSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()
    class Meta:
        model = VehicleSale
        fields = ["cost_price", "sale_price", "vehicle"]

    def create(self, validated_data):
        vehicle = validated_data.pop("vehicle", {})
        if vehicle:
            images = vehicle.pop('images', [])
            docs = vehicle.pop('documents', [])
            create_base_vehicle = BaseVehicle.objects.create(**vehicle)
            if images:
                [Image.create_file(image, create_base_vehicle) for image in images]
            if docs:
                [Documents.create_file(docs, create_base_vehicle) for doc in docs]
        create_vehicle_sale = VehicleRent.objects.create(**validated_data, vehicle=create_base_vehicle)
        return create_vehicle_sale
    
    def update(self, instance, validated_data):
        vehicle = validated_data.pop("vehicle", {})
        instance = super().update(instance, validated_data)
        if vehicle:
            images = vehicle.pop('images', [])
            docs = vehicle.pop("docs", [])
            delete_images = vehicle.pop('delete_images', [])
            update_base_vehicle = instance.vehicle.update(**vehicle)
            if images:
                [Image.create_file(image, instance) for image in images]
            if delete_images:
                Image.objects.filter(pk__in=delete_images).delete()
            if docs:
                [Documents.create_file(doc, instance) for doc in docs]
            if delete_documents:
                Documents.objects.filter(pk__in=delete_documents).delete()
        return instance

class RentSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()
    class Meta:
        model = VehicleRent
        fields = ["price_per_day", "price_per_month", "is_rent", "vehicle"]

    def create(self, validated_data):
        vehicle = validated_data.pop("vehicle", {})
        if vehicle:
            images = vehicle.pop('images', [])
            docs = vehicle.pop('documents', [])
            create_base_vehicle = BaseVehicle.objects.create(**vehicle)
            if images:
                [Image.create_file(image, create_base_vehicle) for image in images]
            if docs:
                [Documents.create_file(docs, create_base_vehicle) for doc in docs]
        create_vehicle_rent = VehicleRent.objects.create(**validated_data, vehicle=create_base_vehicle)
        return create_vehicle_rent
    
    def update(self, instance, validated_data):
        vehicle = validated_data.pop("vehicle", {})
        instance = super().update(instance, validated_data)
        if vehicle:
            images = vehicle.pop('images', [])
            docs = vehicle.pop("docs", [])
            delete_images = vehicle.pop('delete_images', [])
            update_base_vehicle = instance.vehicle.update(**vehicle)
            if images:
                [Image.create_file(image, instance) for image in images]
            if delete_images:
                Image.objects.filter(pk__in=delete_images).delete()
            if docs:
                [Documents.create_file(doc, instance) for doc in docs]
            if delete_documents:
                Documents.objects.filter(pk__in=delete_documents).delete()
        return instance