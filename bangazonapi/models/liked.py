from django.db import models
from .customer import Customer
from .product import Product

class Liked(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING,)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='liked_product')
