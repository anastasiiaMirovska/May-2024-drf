from django_filters import rest_framework as filters

from django.db.models import QuerySet
from django.http import QueryDict

from rest_framework.exceptions import ValidationError

from apps.pizza.models import DaysChoices, PizzaModel
from apps.pizza.serializers import PizzaSerializer


class PizzaFilter(filters.FilterSet):
    #name
    name_starts_with = filters.CharFilter(field_name='name', lookup_expr='startswith')
    name_ends_with = filters.CharFilter(field_name='name', lookup_expr='endswith')
    name_contains = filters.CharFilter(field_name='name', lookup_expr='contains')

    # size
    size_lt = filters.NumberFilter(field_name='size', lookup_expr='lt')
    size_gt = filters.NumberFilter(field_name='size', lookup_expr='gt')
    size_gte = filters.NumberFilter(field_name='size', lookup_expr='gte')
    size_lte = filters.NumberFilter(field_name='size', lookup_expr='lte')

    # price
    price_lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    price_gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_lte = filters.NumberFilter(field_name='price', lookup_expr='lte')

    # day
    day_starts_with = filters.CharFilter(field_name='day', lookup_expr='startswith')
    day_ends_with = filters.CharFilter(field_name='day', lookup_expr='endswith')
    day_contains = filters.CharFilter(field_name='day', lookup_expr='contains')

    size_range = filters.RangeFilter(field_name='size')  # range_min=2&range_max=100
    price_in = filters.BaseInFilter(field_name='price')  # price_in=30,25,2000
    day = filters.ChoiceFilter('day', choices=DaysChoices.choices)
    order = filters.OrderingFilter(
        fields=PizzaSerializer.Meta.fields # по всіх полях можна буде сортувати
    )

