from django.test import TestCase
from .models import Categories, Products
from django.utils.text import slugify
from decimal import Decimal


class TestCategoriesModel(TestCase):
    """Test suite for the Categories model."""

    def setUp(self):
        self.category = Categories.objects.create(
            id=1,
            name="Electronics",
            description="Category for electronic products."
        )

    def test_category_creation(self):
        """Test that a category can be created successfully."""
        self.assertEqual(self.category.name, "Electronics")
        self.assertEqual(self.category.slug, slugify("Electronics"))
        self.assertEqual(self.category.description, "Category for electronic products.")

    def test_auto_slug_generation(self):
        """Test that the slug is automatically generated if not provided."""
        category = Categories.objects.create(
            id=2,
            name="Home Appliances"
        )
        self.assertEqual(category.slug, slugify("Home Appliances"))

    def test_str_representation(self):
        """Test the string representation of the category."""
        self.assertEqual(str(self.category), f"{self.category.id} -- {self.category.name} -- {self.category.created_at}")

    def test_meta_options(self):
        """Test the Meta options of the Categories model."""
        self.assertEqual(Categories._meta.verbose_name, "Category")
        self.assertEqual(Categories._meta.verbose_name_plural, "Categories")
        self.assertEqual(Categories._meta.ordering, ['name'])


class ProductsModelTest(TestCase):
    """Test suite for the Products model."""

    def setUp(self):
        self.category = Categories.objects.create(
            id=1,
            name="Electronics",
            description="Category for electronic products."
        )
        self.product = Products.objects.create(
            name="Smartphone",
            description="A high-end smartphone.",
            price=Decimal("999.99"),
            stock=10,
            category=self.category
        )

    def test_product_creation(self):
        """Test that a product can be created successfully."""
        self.assertEqual(self.product.name, "Smartphone")
        self.assertEqual(self.product.slug, slugify("Smartphone"))
        self.assertEqual(self.product.description, "A high-end smartphone.")
        self.assertEqual(self.product.price, Decimal("999.99"))
        self.assertEqual(self.product.stock, 10)
        self.assertEqual(self.product.category, self.category)
        self.assertTrue(self.product.is_active)

    def test_auto_slug_generation(self):
        """Test that the slug is automatically generated if not provided."""
        product = Products.objects.create(
            name="Laptop",
            price=Decimal("1299.99"),
            stock=5,
            category=self.category
        )
        self.assertEqual(product.slug, slugify("Laptop"))

    def test_in_stock_property(self):
        """Test the in_stock property of the product."""
        self.assertTrue(self.product.in_stock)
        self.product.stock = 0
        self.product.save()
        self.assertFalse(self.product.in_stock)

    def test_str_representation(self):
        """Test the string representation of the product."""
        self.assertEqual(str(self.product), f"{self.product.name} -- {self.product.price}")

    def test_category_relationship(self):
        """Test the relationship between Products and Categories."""
        self.assertEqual(self.product.category, self.category)
        self.assertIn(self.product, self.category.products.all())

    def test_meta_options(self):
        """Test the Meta options of the Products model."""
        self.assertEqual(Products._meta.verbose_name, "Product")
        self.assertEqual(Products._meta.verbose_name_plural, "Products")
        self.assertEqual(Products._meta.ordering, ['-created_at'])
