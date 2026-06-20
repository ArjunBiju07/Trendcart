from customers.models import Customer
from products.models import Products
from django.db import models

# Orders models

class Orders(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICE = ((LIVE,'Live'),(DELETE,'Delete'))
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELEVERED = 3
    ORDER_REJECTED = 4
    STATUS_CHOICE = (
        (ORDER_PROCESSED,'ORDER_PROCESSED'),
        (ORDER_DELEVERED,'ORDER_DELEVERED'),
        (ORDER_REJECTED,'ORDER_REJECTED')
    )
    order_status = models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    owner = models.ForeignKey(Customer,on_delete=models.SET_NULL,related_name='orders',null = True)
    delete_status = models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderedItems(models.Model):
    products = models.ForeignKey(Products,on_delete=models.SET_NULL,related_name='added_carts',null = True)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Orders,on_delete=models.CASCADE,related_name="added_items")
