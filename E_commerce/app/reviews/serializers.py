from rest_framework import serializers

from .models import Reviews


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
    
    read_only_fields = ('id', 'created_at', 'updated_at')
