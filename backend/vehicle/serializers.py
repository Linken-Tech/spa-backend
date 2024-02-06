from pyexpat import model
from pkg_resources import require
from rest_framework import serializers
import vehicle
from vehicle.models import *
from django.core.exceptions import ObjectDoesNotExist
    
class VehicleBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleBrand
        fields = '__all__'

class VehicleDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleDocument
        fields = ['id','document']

class DownloadVehicleDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleDocument
        fields = ['id','document', 'vehicle']

class VehicleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleImage
        fields = ['id','vehicle_image']

# class VehicleRentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = VehicleRent
#         fields = ['id', 'price_per_day', 'price_per_month', 'is_active']

class VehicleSerializer(serializers.ModelSerializer):
    accessories = serializers.ListField(write_only=True)
    vehicle_documents = serializers.ListField(write_only=True, required=False)
    vehicle_images = serializers.ListField(write_only=True, required=False)
    delete_documents = serializers.ListField(write_only=True, required=False)
    delete_images = serializers.ListField(write_only=True, required=False)
    # vehicle_rent = VehicleRentSerializer(write_only=True, required=False)
    
    class Meta:
        model = Vehicle
        fields = ['id', 'vehicle', 'vehicle_brand', 'vehicle_overview', 'number_plate', 'price_per_day', 'price_per_month', 'price_of_cost', 'price_of_sale', 'fuel_type', 'model_year', 'seating_capacity', 'mileage', 'accessories', 'vehicle_documents', 'vehicle_images', 'delete_documents', 'delete_images']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['vehicle_brand'] = VehicleBrandSerializer(instance.vehicle_brand).data
        representation['accessories'] = instance.accessories
        request = self.context.get('request').data
        # if instance.vehicle_rent != None or (request.get('vehicle_rent.price_per_day') and request.get('vehicle_rent.price_per_month')):
        #     representation['vehicle_rent'] = VehicleRentSerializer(instance.vehicle_rent).data
        representation['vehicle_documents'] = VehicleDocumentSerializer(instance.documents.all(), many=True).data
        representation['vehicle_images'] = VehicleImageSerializer(instance.vehicle_image.all(), many=True).data
        return representation

    def create(self, validated_data):
        car_doc = validated_data.pop('vehicle_documents', [])
        car_images = validated_data.pop('vehicle_images', [])
        rent_details = validated_data.pop('vehicle_rent', {})
        create_vehicle = super().create(validated_data)
    
        if car_doc:
            create_vehicle_doc = create_vehicle.documents.bulk_create([VehicleDocument(document=doc, vehicle=create_vehicle) for doc in car_doc])
        if car_images:
            create_vehicle_image = create_vehicle.vehicle_image.bulk_create(VehicleImage(vehicle_image=image, vehicle=create_vehicle) for image in car_images)
        # if rent_details:
        #     rent = VehicleRent.objects.create(price_per_day=rent_details.get('price_per_day'), price_per_month=rent_details.get('price_per_month'))
        #     create_vehicle.vehicle_rent = rent
        #     create_vehicle.save()

        return create_vehicle

    def update(self, instance, validated_data):
        car_doc = validated_data.pop('vehicle_documents', [])
        car_images = validated_data.pop('vehicle_images', [])
        delete_doc = validated_data.pop('delete_documents', [])
        delete_images = validated_data.pop('delete_images', [])
        rent_details = validated_data.pop('vehicle_rent', {})
        instance = super().update(instance, validated_data)
        
        if car_doc:
            update_vehicle_doc = instance.documents.bulk_create([VehicleDocument(document=doc, vehicle=instance) for doc in car_doc])
        if car_images:
            update_vehicle_image = instance.vehicle_image.bulk_create(VehicleImage(vehicle_image=image, vehicle=instance) for image in car_images)
        # if rent_details:
        #     instance.vehicle_rent.price_per_day=rent_details.get('price_per_day')
        #     instance.vehicle_rent.price_per_month=rent_details.get('price_per_month')
        #     instance.vehicle_rent.save()
            
        if delete_doc:
            instance.documents.filter(id__in=delete_doc).delete()
        if delete_images:
            instance.vehicle_image.filter(id__in=delete_images).delete()
            
        return instance
