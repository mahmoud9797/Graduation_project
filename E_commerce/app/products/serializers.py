from rest_framework import serializers
from .models import Products, Categories


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        feilds = '__all__'

        read_only_fields = ('id', 'created_at', 'updated_at')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

        read_only_fields = ('id', 'created_at', 'updated_at')
