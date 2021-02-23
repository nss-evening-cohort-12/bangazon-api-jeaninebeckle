from django.urls import path
from .views.products import highproductprice_list, lowproductprice_list



urlpatterns = [
    path('reports/highproductprice', highproductprice_list),
    path('reports/lowproductprice', lowproductprice_list)
]
