from django.shortcuts import render
from django.views import View
from user.models import CustomerUser
from product.models import Category
# Create your views here.

class HomeView(View):
    def get(seft, request):
        qs1 = Category.objects.values("id", "title")
        if 'cart' in request.session:
            cartInfo = len(request.session['cart'])
        else:
            cartInfo = 0
        print(cartInfo)
        if request.user.is_authenticated:
            checkAdmin = request.user.is_superuser
            user = CustomerUser.objects.get(id=request.user.id)
            return render(request,'homepage/index.html', {'user': user,'category_title':qs1, 'checkAdmin': checkAdmin, "cart": cartInfo})
        return render(request,'homepage/index.html', {'category_title':qs1, "cart": cartInfo})