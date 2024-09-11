from django.urls import path
from .views import product_list
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('api/products/', product_list, name='product-list'),
]

