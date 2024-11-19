from django.db import models # type: ignore

# Create your models here.
class Orders(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    order_item = models.CharField(max_length=100)
    order_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_address = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    estimated_delivery_time = models.TimeField()
    
    def __str__(self):
        return self.order_item 


class Customer(models.Model):
    customer_id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name
    
class Restaurant(models.Model):
    restaurant_id = models.BigAutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=100)
    restaurant_address = models.CharField(max_length=100)
    restaurant_email = models.EmailField(max_length=100)

class Delivery_Driver(models.Model):
    driver_id = models.BigAutoField(primary_key=True)
    driver_fname = models.CharField(max_length= 100)
    driver_lname = models.CharField(max_length= 100)
    driver_phone_number = models.IntegerField()
    vehicle_type = models.CharField(max_length= 100)
    license_plate = models.CharField(max_length= 20)

class Menu(models.Model):
    menu_id = models.BigAutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=500)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    restaurant_name2 = models.CharField(max_length=100)
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)

    def __str__(self):
        return self.item_name