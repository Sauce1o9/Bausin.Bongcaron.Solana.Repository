from django.contrib import admin # type: ignore
from .models import Orders, Customer, Restaurant, Delivery_Driver # Ensure Customer is imported

# Register your models here.
admin.site.register(Orders)
admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(Delivery_Driver)