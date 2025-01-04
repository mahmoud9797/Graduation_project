from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): 
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'users'

    def __str__(self):
        return self.email