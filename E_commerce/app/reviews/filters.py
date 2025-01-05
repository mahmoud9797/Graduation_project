import django_filters as filters
from .models import Reviews

class ReviewFilter(filters.FilterSet):
    class Meta:
        model = Reviews
        fields = {
            'product': ['exact'],
            'rating': ['exact'],
        }
