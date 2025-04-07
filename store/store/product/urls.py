from django.urls import path
from .views import add_to_cart
from . import views

urlpatterns = [
    path('', views.ProductGridView.as_view(), name='product-grid'),  
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),  
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add-to-cart'),
]