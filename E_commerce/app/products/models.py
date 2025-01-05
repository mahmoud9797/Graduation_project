"""product models for categories and products in the api"""
from django.db import models
from django.utils.text import slugify
# Create your models here.


class Categories(models.Model):
    """
    Represents a product category in the e-commerce application.

    Attributes:
        id (PositiveIntegerField): The unique primary key for the category.
        name (CharField): The name of the category, up to 255 characters.
        slug (SlugField): A URL-friendly identifier, auto-generated from the name if not provided.
        description (TextField): An optional detailed description of the category.
        created_at (DateTimeField): The date and time the category was created (auto-generated).
        updated_at (DateTimeField): The date and time the category was last updated (auto-generated).
    """

    id = models.PositiveIntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=255, null=False)
    slug = models.SlugField(null=False, unique=True, blank=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        """
        Returns a string representation of the category object.

        Returns:
            str: The category ID, name, and creation timestamp.
        """

        return f"{self.id} -- {self.name} -- {self.created_at}"
    
    def save(self, *args, **kwargs):
        """
        Overridden save method to auto-generate the slug field 
        from the name if the slug is not provided.
        """

        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    class Meta:
        """
        Meta options for the Categories model.

        Attributes:
            ordering (list): Specifies default ordering by name (alphabetical).
            verbose_name (str): The human-readable name of the model in singular form.
            verbose_name_plural (str): The human-readable name of the model in plural form.
        """

        ordering = ['name']
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Products(models.Model):
    """
    Represents a product in the e-commerce application.

    Attributes:
        id (AutoField): The unique primary key for the product (auto-incremented).
        name (CharField): The name of the product, up to 255 characters.
        slug (SlugField): A URL-friendly identifier, unique for each product.
        description (TextField): An optional detailed description of the product.
        price (DecimalField): The price of the product with up to 12 digits and 2 decimal places.
        stock (PositiveIntegerField): The available stock quantity of the product.
        category_id (ForeignKey): A foreign key linking the product to its category.
        image (ImageField): An optional product image stored in the 'products-images/' directory.
        is_active (BooleanField): Indicates whether the product is active (defaults to True).
        created_at (DateTimeField): The date and time the product was created (auto-generated).
        updated_at (DateTimeField): The date and time the product was last updated (auto-generated).
    """

    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=255, null=False)
    slug = models.SlugField(unique=True, null=False)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    stock = models.PositiveIntegerField(null=False, default=0)
    category = models.ForeignKey(
        Categories, 
        null=False, 
        related_name='products',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='products-images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    @property
    def in_stock(self):
        """
        Returns whether the product is in stock.

        Returns:
            bool: True if the stock is greater than 0, False otherwise.
        """

        return self.stock > 0

    def save(self, *args, **kwargs):
        """
        Overridden save method to auto-generate the slug field 
        from the name if the slug is not provided.
        """

        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the product object.

        Returns:
            str: The product name and price.
        """

        return f"{self.name} -- {self.price}"

    class Meta:
        """
        Meta options for the Products model.

        Attributes:
            ordering (list): Specifies default ordering by creation date (newest first).
            verbose_name (str): The human-readable name of the model in singular form.
            verbose_name_plural (str): The human-readable name of the model in plural form.
        """

        ordering = ['-created_at']
        verbose_name = "Product"
        verbose_name_plural = "Products"
