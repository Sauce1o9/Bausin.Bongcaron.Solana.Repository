from django import forms # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib.auth.models import User # type: ignore
from .models import Menu, Customer

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['item_name', 'item_description', 'item_price', 'image']  # Include the image field

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_id', 'password', 'first_name', 'last_name', 'email', 'phone_number', 'address']
