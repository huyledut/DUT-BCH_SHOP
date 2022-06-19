from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Order, OrderDetail
from .forms import OrderForm, OrderDetailForm
from django.views import View
# Create your views here.

def CreateOrder(request):
    temp_cart = request.session['cart']
    del request.session['cart']
    cart = {}
    if 'cart' in request.session:
        request.session['cart'] = cart
    if request.method == "POST":
        name = request.POST["name_receive"]
        phone = request.POST["phone_number"]
        user = request.user.id
        add = request.POST["address_receive"]
        des = request.POST["description"]
        order = Order(user = user, phone_number = phone, shipping_address = add, order_description = des, name_receive = name)
        order.save()
        
        for key, value in temp_cart.items():
            orderDetail = OrderDetail(order_id= order.id, pro_id = temp_cart[key]['id'], number = temp_cart[key]['number'], address_delivery = add)
            orderDetail.save()
        return redirect('/product/')
    else:
        return HttpResponse('Invalid data input')
