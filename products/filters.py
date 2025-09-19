import django_filters
from .models import Product
from django.db.models import Q

class ProductFilter(django_filters.FilterSet):
    max_price = django_filters.NumberFilter(field_name='price',lookup_expr='lte',required=False)
    min_price = django_filters.NumberFilter(field_name='price',lookup_expr='gte',required=False)
    category = django_filters.CharFilter(field_name='category__name',lookup_expr='icontains',required=False)
    search = django_filters.CharFilter(method='filter_search', required=False)
    
    class Meta:
        model = Product
        fields = ['max_price','min_price','category','search']

    def filter_search(self, queryset, name, value):
        if not value:
            return queryset  # No filtering if search is empty
        return queryset.filter(
            Q(name__icontains=value) | Q(category__name__icontains=value)
        )