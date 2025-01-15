from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from .filters import ProductFilter
from .models import Products, Categories
from app.orders.models import OrderItem, Order
from app.reviews.models import Reviews

from .serializers import ProductSerializer, CategorySerializer
from app.reviews.serializers import ReviewSerializer
from app.orders.serializer import OrderItemSerializer
from .premission import IsAdminUser

class CategoryCreateListAPIView(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

categories_list = CategoryCreateListAPIView.as_view()


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        try:
            category = Categories.objects.get(slug=slug)
        except Categories.DoesNotExist:
            raise NotFound(f"this category {slug} nas not been added")

        return Products.objects.filter(category=category)

Categories_list_view = CategoryListAPIView.as_view()


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ProductFilter
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        return super().get_permissions()

product_list_create_view = ProductListCreateAPIView.as_view()

class AddToCartAPIView(generics.CreateAPIView):
    """
    Add a product to the cart or update its quantity if it already exists in the cart.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = OrderItemSerializer

    def create(self, request, *args, **kwargs):
        try:
            product = Products.objects.get(slug=kwargs.get("slug"))
        except Products.DoesNotExist:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the product has sufficient stock
        if product.stock < 1:
            return Response({"error": "Product is out of stock."}, status=status.HTTP_400_BAD_REQUEST)

        # Get or create a pending order for the authenticated user
        order, created = Order.objects.get_or_create(
            user=request.user,
            status='pending',
            defaults={"total_amount": 0, "shipping_address": ""}
        )

        # Check if the product is already in the order
        order_item, item_created = OrderItem.objects.get_or_create(
            order=order,
            Products=product,
            defaults={"quantity": 1, "price": product.price}
        )

        if not item_created:
            # If the item exists, check if there's enough stock for an additional unit
            if product.stock < (order_item.quantity + 1):
                return Response({"error": "Not enough stock available."}, status=status.HTTP_400_BAD_REQUEST)

            # Update the quantity and price
            order_item.quantity += 1
            order_item.price = product.price * order_item.quantity
            order_item.save()

        # Deduct the stock for the added product
        product.stock -= 1
        product.save()

        # Recalculate the order's total amount
        order.total_amount = sum(item.price for item in order.items.all())
        order.save()

        serializer = self.get_serializer(order_item)

        return Response({
            "message": "Product added to cart successfully.",
            "order_id": order.id,
            "order_item": serializer.data,
            "total_amount": str(order.total_amount),
        }, status=status.HTTP_200_OK)

class ProductReviewListAPIView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        try:
            product = Products.objects.get(slug=slug)
        except Products.DoesNotExist:
            raise NotFound(f"Product with slug '{slug}' not found.")
        return Reviews.objects.filter(product=product)

product_review_list_view = ProductReviewListAPIView.as_view()
