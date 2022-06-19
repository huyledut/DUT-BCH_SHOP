from tkinter import TRUE
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField()
    active = models.BooleanField()
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    product_img = models.CharField(max_length=1000, blank=True,null=True )
    image_view = models.ImageField(upload_to='images',default=None,null=False)
    def __str__(self):
        return self.title
class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField(default=0)
    def __str__(self):
        return self.title

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