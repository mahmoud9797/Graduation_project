from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.categories_list, name='categories'), 
    path('products/', views.product_list_view, name='product-list'),
    path('products/<slug:slug>/reviews/', views.product_review_list_view, name='product-reviews'),
    path('categories/<slug:slug>/products/', views.Categories_list_view, name='product-category'),
]
