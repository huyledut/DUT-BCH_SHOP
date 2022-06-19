from unicodedata import category
from django import forms
from .models import Product, Category, Variation, Order, OrderDetail
from user.models import CustomerUser

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widget ={
                category:= forms.ModelChoiceField(
                    queryset=Category.objects.all(), 
                    label="Category",
                    widget=forms.Select(
                                attrs={
                                    'placeholder': 'Product Category', 'class': 'form-control'}),
                                required=True
                    )
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        # self.fields['category'].widget.attrs.update({'style': 'width:100px !important;'})
        self.fields['category'].widget.attrs['style'] = 'width:100px !important;'
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['active'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['product_img'].widget.attrs.update({'class': 'form-control'})
        self.fields['image_view'].widget.attrs.update({'class': 'form-control'})

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widget ={
                category:= forms.ModelChoiceField(
                    queryset=Category.objects.all(), 
                    label="Category",
                    widget=forms.Select(
                                attrs={
                                    'placeholder': 'Product Category', 'class': 'form-control'}),
                                required=True
                    )
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['slug'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['active'].widget.attrs.update({'class': 'form-check-input'})

class VariationFrom(forms.ModelForm):
    class Meta:
        model = Variation
        fields = '__all__'
        widget ={
                category:= forms.ModelChoiceField(
                    queryset=Variation.objects.all(), 
                    label="Variation",
                    widget=forms.Select(
                                attrs={
                                    'placeholder': 'Product Category', 'class': 'form-control'}),
                                required=True
                    )
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['product'].widget.attrs.update({'class': 'product'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['active'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['sale_price'].widget.attrs.update({'class': 'form-control'})
        self.fields['inventory'].widget.attrs.update({'class': 'form-control'})


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        widget ={
                user:= forms.ModelChoiceField(
                    queryset = CustomerUser.objects.all(), 
                    label="User",
                    widget=forms.Select(
                                attrs={
                                    'placeholder': 'CustomerUser', 'class': 'form-control'}),
                                required=True
                    )
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['style'] = 'width:100px !important;'
        self.fields['name_receive'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['shipping_address'].widget.attrs.update({'class': 'form-control'})
        self.fields['order_description'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_completed'].widget.attrs.update({'class': 'form-check-input'})

class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = "__all__"
        widget ={
                order:= forms.ModelChoiceField(
                    queryset = Order.objects.all(), 
                    label="Order",
                    widget=forms.Select(
                                attrs={
                                    'placeholder': 'Order', 'class': 'form-control'}),
                                required=True
                    ),
                product:= forms.ModelChoiceField(
                    queryset = Product.objects.all(), 
                    label="Product",
                    widget=forms.Select(
                                attrs={
                                    'placeholder': 'Product', 'class': 'form-control'}),
                                required=True
                    )
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order_id'].widget.attrs['style'] = 'width:100px !important;'
        self.fields['pro_id'].widget.attrs['style'] = 'width:100px !important;'
        self.fields['number'].widget.attrs.update({'class': 'form-control'})
        self.fields['address_delivery'].widget.attrs.update({'class': 'form-control'})
