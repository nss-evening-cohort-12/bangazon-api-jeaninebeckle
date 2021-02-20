from django.urls import path
from .views.products import highproductprice_list



urlpatterns = [
    path('reports/highproductprice', highproductprice_list)
]
