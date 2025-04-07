"""
URL configuration for store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from user import views as user
from .views import home_view
from .views import about_view
from .views import contact_view
from cart.views import cart_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path("products/", include('product.urls')),
    path('cart/', cart_view, name='cart'),
    path('orders/', include('order.urls')), 
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', user.create_user, name='register'),
]

