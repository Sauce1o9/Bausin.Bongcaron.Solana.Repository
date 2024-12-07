from django.contrib import admin # type: ignore
from .models import Orders, Customer, Delivery_Driver, Menu, Checkout# Ensure Customer is imported
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Orders)
admin.site.register(Customer)
admin.site.register(Checkout)

class MenuAdmin(ImportExportModelAdmin):
    ...

admin.site.register(Menu, MenuAdmin)

class Delivery_DriverAdmin(ImportExportModelAdmin):
    ...

admin.site.register(Delivery_Driver, Delivery_DriverAdmin)