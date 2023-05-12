from django.urls import path
from sales.views import create_sale, get_sales

urlpatterns = [
    path('api/sales/', create_sale),
    path('api/sales/list/', get_sales),
    # Add more URL patterns for other APIs
]
