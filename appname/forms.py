from django.forms import ModelForm

from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


from django import forms
from .models import Image, Product


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class OrdervForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['order_status', 'items']




