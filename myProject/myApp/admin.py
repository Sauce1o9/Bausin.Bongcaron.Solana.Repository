from django.contrib import admin # type: ignore
from .models import Orders, Customer, Delivery_Driver, Menu, Checkout# Ensure Customer is imported

# Register your models here.
admin.site.register(Orders)
admin.site.register(Customer)
admin.site.register(Delivery_Driver)
admin.site.register(Menu)
admin.site.register(Checkout)