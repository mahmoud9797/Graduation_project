from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import NotFound

from .filters import ProductFilter
from .models import Products, Categories
from app.reviews.models import Reviews
from .serializers import ProductSerializer, CategorySerializer
from app.reviews.serializers import ReviewSerializer


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        try:
            Category = Categories.objects.get(slug=slug)
        except Categories.DoesNotExist:
            raise NotFound(f"this category {slug} nas not been added")
        
        return Products.objects.filter(Category=Category)

Categories_list_view = CategoryListAPIView.as_view()
class ProductListAPIView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ProductFilter

product_list_view = ProductListAPIView.as_view()

class ProductReviewListAPIView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        try:
            product = Products.objects.get(slug=slug)
        except Products.DoesNotExist:
            raise NotFound(f"Product with slug '{slug}' not found.")
        return Reviews.objects.filter(product=product)

product_review_list_view = ProductReviewListAPIView.as_view()
