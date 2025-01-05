from django.test import TestCase
from app.products.models import Products
from app.accounts.models import User
from app.reviews.models import Reviews

class ReviewsModelTest(TestCase):
    def setUp(self):
        # Set up a user
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password123"
        )

        # Set up a product
        self.product = Products.objects.create(
            name="Test Product",
            slug="test-product",
            price=100.00,
            stock=10,
        )

    def test_review_creation(self):
        # Create a review
        review = Reviews.objects.create(
            product=self.product,
            user=self.user,
            rating=5,
            comment="Excellent product!"
        )

        # Verify the review was created successfully
        self.assertEqual(review.product, self.product)
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, "Excellent product!")

    def test_str_representation(self):
        # Create a review
        review = Reviews.objects.create(
            product=self.product,
            user=self.user,
            rating=5,
            comment="Excellent product!"
        )
