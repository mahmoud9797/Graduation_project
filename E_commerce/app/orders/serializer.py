
# apps/orders/serializers.py
from rest_framework import serializers
from .models import Order, OrderItem
from app.products.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'product_id', 'quantity', 'price', 'created_at')
        read_only_fields = ('id', 'created_at')

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    status = serializers.CharField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'items', 'total_amount', 'status', 
                 'shipping_address', 'created_at')
        read_only_fields = ('id', 'created_at')

class OrderCreateSerializer(serializers.ModelSerializer):
    items = serializers.ListField(
        child=serializers.DictField(
            child=serializers.IntegerField()
        ),
        write_only=True
    )
    shipping_address = serializers.CharField()

    class Meta:
        model = Order
        fields = ('items', 'shipping_address')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context['request'].user
        
        # Calculate total amount
        total_amount = 0
        for item in items_data:
            product = product.objects.get(id=item['product_id'])
            total_amount += product.price * item['quantity']

        # Create order
        order = Order.objects.create(
            user=user,
            total_amount=total_amount,
            **validated_data
        )

        # Create order items
        for item in items_data:
            product = product.objects.get(id=item['product_id'])
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item['quantity'],
                price=product.price
            )

        return order

    
      




