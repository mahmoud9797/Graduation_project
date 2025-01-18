# orders/serializers.py
from rest_framework import serializers
from .models import Order, OrderItem
from app.products.models import Products
from app.products.serializers import ProductSerializer  # Import your product serializer

class OrderItemSerializer(serializers.ModelSerializer):
    Products = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'Products', 'product_id', 'quantity', 'price', 'created_at']
        read_only_fields = ['price', 'created_at']

class OrderCreateSerializer(serializers.ModelSerializer):
    items = serializers.ListField(
        child=serializers.DictField(),
        write_only=True
    )

    class Meta:
        model = Order
        fields = ['items', 'shipping_address']

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("No items provided")
        
        for item in value:
            if 'product_id' not in item:
                raise serializers.ValidationError("product_id is required")
            if 'quantity' not in item:
                raise serializers.ValidationError("quantity is required")
            
            try:
                product = Products.objects.get(id=item['product_id'])
                if product.stock < item['quantity']:
                    raise serializers.ValidationError(
                        f"Insufficient stock for product {product.name}"
                    )
            except Products.DoesNotExist:
                raise serializers.ValidationError(
                    f"Product with id {item['product_id']} not found"
                )
        
        return value

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context['request'].user
        
        # Calculate total amount and prepare items
        total_amount = 0
        order_items = []

        for item in items_data:
            product = Products.objects.get(id=item['product_id'])
            quantity = item['quantity']
            price = product.price
            total_amount += price * quantity
            order_items.append({
                'product': product,
                'quantity': quantity,
                'price': price
            })

        # Create order
        order = Order.objects.create(
            user=user,
            total_amount=total_amount,
            **validated_data
        )

        # Create order items
        for item in order_items:
            OrderItem.objects.create(
                order=order,
                Products=item['product'],
                quantity=item['quantity'],
                price=item['price']
            )

        return order

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField()
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'total_amount', 
                 'status', 'shipping_address', 'created_at', 'updated_at']
        read_only_fields = ['user', 'total_amount', 'status', 
                           'created_at', 'updated_at']


