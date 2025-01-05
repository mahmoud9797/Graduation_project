import django_filters as filters

from .models import Products


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    category_name = filters.CharFilter(field_name="category__name", lookup_expr='iexact')
    
    class Meta:
        model = Products
        fields = [
            'min_price',
            'max_price',
            'category_name',
        ]        
