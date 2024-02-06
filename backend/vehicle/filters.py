from django_filters import filters
from django_filters.rest_framework import filterset
from django.db.models import Q
from vehicle.models import Vehicle

class VehicleFilter(filterset.FilterSet):
    vehicle_type = filters.CharFilter(method="filter_vehicle_type", required=False)

    class Meta:
        model = Vehicle
        fields = ["vehicle_type"]

    def filter_vehicle_type(self, queryset, name, value):
        standardize_get_value = value.lower()
        zero_decimal = "{:.2f}".format(0)
        if standardize_get_value == 'sale':
            filter_list = queryset.filter(Q(price_per_day__isnull=True, price_per_month__isnull=True) | Q(price_per_day=zero_decimal, price_per_month=zero_decimal))
        if standardize_get_value == 'rental':
            filter_list = queryset.filter(Q(price_of_sale__isnull=True) | Q(price_of_sale=zero_decimal))
        return filter_list