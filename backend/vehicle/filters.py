from django_filters import filters
from django_filters.rest_framework import filterset
from vehicle.models import VehicleSale, VehicleRent, Brand


class VehicleSaleFilter(filterset.FilterSet):
    brand = filters.CharFilter(method="filter_brand", required=False)
    model_year = filters.CharFilter(method="filter_model_year", required=False)

    class Meta:
        model = VehicleSale
        fields = ["brand", "model_year"]

    def filter_brand(self, queryset, name, value):
        get_brand = Brand.objects.filter(brand_name=value)
        if get_brand:
            filter_list = queryset.filter(vehicle__brand=get_brand)
        return filter_list

    def filter_model_year(self, queryset, name, value):
        filter_list = queryset.filter(vehicle__model_year=value)
        return filter_list


class VehicleRentFilter(filterset.FilterSet):
    brand = filters.CharFilter(method="filter_brand", required=False)
    model_year = filters.CharFilter(method="filter_model_year", required=False)

    class Meta:
        model = VehicleRent
        fields = ["brand", "model_year"]

    def filter_brand(self, queryset, name, value):
        get_brand = Brand.objects.filter(brand_name=value)
        if get_brand:
            filter_list = queryset.filter(vehicle__brand=get_brand)
            return filter_list

    def filter_model_year(self, queryset, name, value):
        filter_list = queryset.filter(vehicle__model_year=value)
        return filter_list
