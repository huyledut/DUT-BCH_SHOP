from django.contrib import admin
from .models import Product, Category, Variation, Order, OrderDetail
# Register your models here.
admin.site.register(Product)
admin.site.register(Variation)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderDetail)
