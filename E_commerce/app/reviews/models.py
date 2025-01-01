from django.db import models
from app.products.models import Products
from app.accounts.models import User
# Create your models here.


class Reviews(models.Model):
    id = models.BigAutoField(null=False, primary_key=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='reviews', null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', null=False)
    rating = models.PositiveIntegerField(null=False)
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Review: {self.rating}--{self.product}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
