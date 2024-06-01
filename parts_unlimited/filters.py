import django_filters
from .models import Part


class PartFilter(django_filters.FilterSet):
    is_active = django_filters.BooleanFilter()

    class Meta:
        model = Part
        fields = ['is_active']
