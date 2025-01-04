from django.db import models
from app.products.models import Products
from app.accounts.models import User
# Create your models here.


class Reviews(models.Model):

    RATING_CHOICES = (
        (1, "1 star"),
        (2, "2 stars"),
        (3, "3 stars"),
        (4, "4 stars"),
        (5, "5 stars")
    )
    id = models.BigAutoField(null=False, primary_key=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='reviews', null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', null=False)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Review: {self.rating}--{self.product}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
