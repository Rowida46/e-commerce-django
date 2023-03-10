"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from products.views import *


urlpatterns = [
    path('home', productView, name="productView"),
    path("products", lst_products, name="lst_products"),
    path('product/<int:id>', product_details, name='productDetails'),
    # path('product/<slug:slug>', product_details, name='productDetails'),
    path("notFound/<msg>", not_found, name="not_found"),
    path('<int:id>/delete', deleteProduct, name='delete_product'),
    path('<int:id>/edit', edit_product, name='edit_product'),
    path('create', create_product, name='create_product'),
    # path('search', Search_by_title.as_view(), name="search_results")
    path("search", search_by_title, name="search_results")



]
