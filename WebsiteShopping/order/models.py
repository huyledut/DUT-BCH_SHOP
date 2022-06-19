from pyexpat import model
from django.db import models
from  user.models import CustomerUser
from product.models import Product
from cart.models import Cart
# Create your models here.
class Order(models.Model):
    user = models.IntegerField()
    phone_number = models.CharField(max_length=10,default="")
    name_receive = models.CharField(default="", max_length=255)
    shipping_address = models.CharField(max_length=255, default='', null=False)
    order_description = models.TextField(default='', null=False)
    is_completed = models.BooleanField(default=False)
    def __str__(self):
        return self.phone_number

class OrderDetail(models.Model):
    order_id = models.IntegerField(null = False)
    pro_id = models.IntegerField(null = False)
    number = models.IntegerField(default=1, null=False)
    address_delivery = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)