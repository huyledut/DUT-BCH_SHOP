from django.urls import path,include
from . import views

app_name = 'Order'
urlpatterns =[
    path("new-order/", views.CreateOrder, name="new-order"),
]