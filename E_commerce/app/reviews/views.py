from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Reviews
from .filters import ReviewFilter
from .serializers import ReviewSerializer
# Create your views here.


class ReviewListAPIVew(generics.ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ReviewFilter

review_list_view = ReviewListAPIVew.as_view()
