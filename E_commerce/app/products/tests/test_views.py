from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from products.models import Products, Categories
from app.orders.models import Order, OrderItem
from app.reviews.models import Reviews

class ViewsTestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpassword')

        # Create test category and product
        self.category = Categories.objects.create(name='Test Category', slug='test-category')
        self.product = Products.objects.create(
            name='Test Product',
            slug='test-product',
            category=self.category,
            stock=10,
            price=100.0
        )

        # Authenticate user
        self.client = APIClient()
        self.client.login(username='testuser', password='password')

    def test_category_list(self):
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_list(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Product', str(response.data))

    def test_add_to_cart_authenticated(self):
        response = self.client.post(f'/cart/add/{self.product.slug}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Product added to cart successfully.")

    def test_add_to_cart_unauthenticated(self):
        self.client.logout()
        response = self.client.post(f'/cart/add/{self.product.slug}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_add_to_cart_insufficient_stock(self):
        # Simulate insufficient stock
        self.product.stock = 0
        self.product.save()

        response = self.client.post(f'/cart/add/{self.product.slug}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], "Product is out of stock.")

    def test_product_reviews(self):
        # Create a test review
        Reviews.objects.create(
            product=self.product,
            user=self.user,
            rating=5,
            comment="Great product!"
        )

        response = self.client.get(f'/products/{self.product.slug}/reviews/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Great product!", str(response.data))

    def test_create_category_admin_only(self):
        self.client.logout()
        self.client.login(username='admin', password='adminpassword')

        response = self.client.post('/categories/', data={'name': 'New Category', 'slug': 'new-category'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('New Category', str(response.data))

    def test_create_category_non_admin(self):
        response = self.client.post('/categories/', data={'name': 'New Category', 'slug': 'new-category'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
