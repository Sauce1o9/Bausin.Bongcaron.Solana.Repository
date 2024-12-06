from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth import authenticate, login, logout as auth_logout  # type: ignore
from django.contrib import messages # type: ignore
from .forms import MenuForm
from .models import Orders, Customer, Delivery_Driver, Menu, Checkout
from django.http import Http404  # Add this import
import os

# Create your views here.
def Profile(request):
    customer = None
    if 'customer_id' in request.session:
        try:
            customer = Customer.objects.get(customer_id=request.session['customer_id'])
        except Customer.DoesNotExist:
            customer = None

    return render(request, "myApp/Profile.html", {'customer': customer})

def login(request):
    if request.method == 'POST':
        customer_id = request.POST['customer_id']
        password = request.POST['password']
        
        try:
            customer = Customer.objects.get(customer_id=customer_id, password=password)
            request.session['customer_id'] = customer.customer_id  # St            request.session            messages.success(request, 'Login successful')
            return render(request, "myApp/home.html", {'customer': customer})
        except Customer.DoesNotExist:
            messages.error(request, 'Invalid username or password')
            return render(request, "myApp/login.html")

    return render(request, "myApp/login.html")

def logout(request):
    auth_logout(request)
    request.session.pop('customer_id', None)
    messages.success(request, 'You have been logged out.')
    return render(request, "myApp/login.html")

def signup(request):
    if request.method == 'POST':
        customer_id = request.POST['customer_id']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']  # Get the confirm password
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        user_type = request.POST['user_type']  # Get the user type from the form
        customer_image = request.FILES.get('customer_image')  # Get the uploaded image

        # Check password length
        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters long')
            return render(request, "myApp/signup.html")

        # Check if username already exists
        if Customer.objects.filter(customer_id=customer_id).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
            return render(request, "myApp/signup.html")

        # Check if passwords match
        if password != password_confirm:
            messages.error(request, 'Passwords must match')  # Error message
            return render(request, "myApp/signup.html")  # Render the signup page again

        # Create a new Customer instance
        customer = Customer(
            customer_id=customer_id,
            password=password,  # Consider hashing the password
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            address=address,
            user_type=user_type,  # Set the user type
            customer_image=customer_image  # Set the customer image
        )
        customer.save()
        messages.success(request, 'New user added')
        return render(request, "myApp/login.html")
    return render(request, "myApp/signup.html")

def add_order(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')  # Get the item ID from the POST request
        menu_item = get_object_or_404(Menu, pk=item_id)  # Fetch the menu item
        
        # Retrieve the delivery address from the logged-in customer
        delivery_address = None
        order_customer = None  # Initialize order_customer
        if 'customer_id' in request.session:
            try:
                customer = Customer.objects.get(customer_id=request.session['customer_id'])
                delivery_address = customer.address  # Get the customer's address
                order_customer = customer.customer_id  # Get the customer_id for the order
            except Customer.DoesNotExist:
                delivery_address = ''  # Fallback if customer does not exist

        # Create a new order
        order = Orders(
            order_name=menu_item.item_name,
            order_description=menu_item.item_description,
            order_price=menu_item.item_price,
            orders_image=menu_item.image if menu_item.image else None,  # Set the image if it exists
            delivery_address=delivery_address,  # Use the customer's address
            order_customer=order_customer  # Associate the order with the customer
        )
        order.save()  # Save the order to the database
        messages.success(request, 'Order added successfully!')
        return redirect('Orders')  # Redirect back to the Orders page

    return redirect('Orders')  # Redirect if not a POST request

def delete_order(request, order_id):
    order_item = get_object_or_404(Orders, pk=order_id)
    order_item.delete()
    messages.success(request, 'Order removed successfully!')
    return redirect('Orders')

def home(request):
    customer = None
    if 'customer_id' in request.session:
        try:
            customer = Customer.objects.get(customer_id=request.session['customer_id'])
        except Customer.DoesNotExist:
            customer = None

    return render(request, "myApp/home.html", {'customer': customer})

def orders_list(request):
    customer = None
    if 'customer_id' in request.session:
        try:
            customer = Customer.objects.get(customer_id=request.session['customer_id'])
        except Customer.DoesNotExist:
            customer = None

    orders = Orders.objects.all()  # Fetch all orders from the database
    drivers = Delivery_Driver.objects.all()  # Fetch all delivery drivers
    context = {'orders': orders, 'customer': customer, 'drivers': drivers}  # Pass drivers to the template
    return render(request, "myApp/Orders.html", context)  # Pass orders to the template

def checkout_view(request):
    customer = None
    checkout_items = None
    subtotal = 0
    delivery_fee = 29

    if 'customer_id' in request.session:
        try:
            customer = Customer.objects.get(customer_id=request.session['customer_id'])
            checkout_items = Checkout.objects.filter(checkout_customer=customer.customer_id)
            
            # Calculate subtotal for this customer's items
            subtotal = sum(item.checkout_price for item in checkout_items)
            
        except Customer.DoesNotExist:
            customer = None

    total = subtotal + delivery_fee
    context = {
        'customer': customer,
        'checkout_items': checkout_items,
        'subtotal': subtotal,
        'delivery_fee': delivery_fee,
        'total': total
    }
    return render(request, "myApp/Checkout.html", context)

def Drivers(request):
    customer = None
    user_type = None
    if 'customer_id' in request.session:
        try:
            customer = Customer.objects.get(customer_id=request.session['customer_id'])
            user_type = customer.user_type
        except Customer.DoesNotExist:
            customer = None

    drivers = Delivery_Driver.objects.all()  # Fetch all delivery drivers
    context = {'drivers': drivers, 'customer': customer, 'user_type': user_type}
    return render(request, "myApp/Drivers.html", context)

def McDonalds(request):
    customer = None
    user_type = None
    if 'customer_id' in request.session:
        try:
            customer = Customer.objects.get(customer_id=request.session['customer_id'])
            user_type = customer.user_type
        except Customer.DoesNotExist:
            customer = None

    menu_items = Menu.objects.filter(restaurant_name2="McDonalds")
    context = {'menu_items': menu_items, 'customer': customer, 'user_type': user_type}
    return render(request, "myApp/McDonalds.html", context)

def Jollibee(request):
    customer = None
    user_type = None
    if 'customer_id' in request.session:
        try:
            customer = Customer.objects.get(customer_id=request.session['customer_id'])
            user_type = customer.user_type
        except Customer.DoesNotExist:
            customer = None

    menu_items = Menu.objects.filter(restaurant_name2="Jollibee")
    context = {'menu_items': menu_items, 'customer': customer, 'user_type': user_type}
    return render(request, "myApp/Jollibee.html", context)

def KFC(request):
    customer = None
    user_type = None
    if 'customer_id' in request.session:
        try:
            customer = Customer.objects.get(customer_id=request.session['customer_id'])
            user_type = customer.user_type
        except Customer.DoesNotExist:
            customer = None

    menu_items = Menu.objects.filter(restaurant_name2="KFC")
    context = {'menu_items': menu_items, 'customer': customer, 'user_type': user_type}
    return render(request, "myApp/KFC.html", context)

def BurgerKing(request):
    customer = None
    user_type = None
    if 'customer_id' in request.session:
        try:
            customer = Customer.objects.get(customer_id=request.session['customer_id'])
            user_type = customer.user_type
        except Customer.DoesNotExist:
            customer = None

    menu_items = Menu.objects.filter(restaurant_name2="BurgerKing")
    context = {'menu_items': menu_items, 'customer': customer, 'user_type': user_type}
    return render(request, "myApp/BurgerKing.html", context)

def Chowking(request):
    customer = None
    user_type = None
    if 'customer_id' in request.session:
        try:
            customer = Customer.objects.get(customer_id=request.session['customer_id'])
            user_type = customer.user_type
        except Customer.DoesNotExist:
            customer = None

    menu_items = Menu.objects.filter(restaurant_name2="Chowking")
    context = {'menu_items': menu_items, 'customer': customer, 'user_type': user_type}
    return render(request, "myApp/Chowking.html", context)

def Greenwich(request):
    customer = None
    user_type = None
    if 'customer_id' in request.session:
        try:
            customer = Customer.objects.get(customer_id=request.session['customer_id'])
            user_type = customer.user_type
        except Customer.DoesNotExist:
            customer = None

    menu_items = Menu.objects.filter(restaurant_name2="Greenwich")
    context = {'menu_items': menu_items, 'customer': customer, 'user_type': user_type}
    return render(request, "myApp/Greenwich.html", context)

def MangInasal(request):
    customer = None
    user_type = None
    if 'customer_id' in request.session:
        try:
            customer = Customer.objects.get(customer_id=request.session['customer_id'])
            user_type = customer.user_type
        except Customer.DoesNotExist:
            customer = None

    menu_items = Menu.objects.filter(restaurant_name2="MangInasal")
    context = {'menu_items': menu_items, 'customer': customer, 'user_type': user_type}
    return render(request, "myApp/MangInasal.html", context)

def PizzaHut(request):
    customer = None
    user_type = None
    if 'customer_id' in request.session:
        try:
            customer = Customer.objects.get(customer_id=request.session['customer_id'])
            user_type = customer.user_type
        except Customer.DoesNotExist:
            customer = None

    menu_items = Menu.objects.filter(restaurant_name2="PizzaHut")
    context = {'menu_items': menu_items, 'customer': customer, 'user_type': user_type}
    return render(request, "myApp/PizzaHut.html", context)


#McDonalds-----------------------------------------------------------------------------------------------
def edit_menu(request, menu_id):
    menu_item = get_object_or_404(Menu, pk=menu_id)
    
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('McDonalds')
    else:
        form = MenuForm(instance=menu_item)
    
    return render(request, "myApp/edit_menu.html", {'form': form, 'menu_item': menu_item})

def delete_menu(request, menu_id):
    menu_item = get_object_or_404(Menu, pk=menu_id)
    menu_item.delete()
    return redirect('McDonalds')

def add_menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.restaurant_name2 = "McDonalds"
            menu_item.save()
            return redirect('McDonalds')
    else:
        form = MenuForm()
    
    return render(request, 'myApp/add_menu.html', {'form': form})


#Jollibee-----------------------------------------------------------------------------------------------
def edit_menu_jollibee(request, menu_id):
    menu_item = get_object_or_404(Menu, pk=menu_id)
    
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('Jollibee')
    else:
        form = MenuForm(instance=menu_item)
    
    return render(request, "myApp/edit_menu_jollibee.html", {'form': form, 'menu_item': menu_item})

def delete_menu_jollibee(request, menu_id):
    menu_item = get_object_or_404(Menu, pk=menu_id)
    menu_item.delete()
    return redirect('Jollibee')

def add_menu_jollibee(request):
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.restaurant_name2 = "Jollibee"
            menu_item.save()
            return redirect('Jollibee')
    else:
        form = MenuForm()
    
    return render(request, 'myApp/add_menu_jollibee.html', {'form': form})


#KFC-----------------------------------------------------------------------------------------------
def edit_menu_kfc(request, menu_id):
    menu_item = get_object_or_404(Menu, pk=menu_id)
    
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('KFC')
    else:
        form = MenuForm(instance=menu_item)
    
    return render(request, "myApp/edit_menu_kfc.html", {'form': form, 'menu_item': menu_item})

def delete_menu_kfc(request, menu_id):
    menu_item = get_object_or_404(Menu, pk=menu_id)
    menu_item.delete()
    return redirect('KFC')

def add_menu_kfc(request):
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.restaurant_name2 = "KFC"
            menu_item.save()
            return redirect('KFC')
    else:
        form = MenuForm()
    
    return render(request, 'myApp/add_menu_kfc.html', {'form': form})



#BurgerKing-----------------------------------------------------------------------------------------------
def edit_menu_burgerking(request, menu_id):
    menu_item = get_object_or_404(Menu, pk=menu_id)
    
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('BurgerKing')
    else:
        form = MenuForm(instance=menu_item)
    
    return render(request, "myApp/edit_menu_burgerking.html", {'form': form, 'menu_item': menu_item})

def delete_menu_burgerking(request, menu_id):
    menu_item = get_object_or_404(Menu, pk=menu_id)
    menu_item.delete()
    return redirect('BurgerKing')

def add_menu_burgerking(request):
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.restaurant_name2 = "BurgerKing"
            menu_item.save()
            return redirect('BurgerKing')
    else:
        form = MenuForm()
    
    return render(request, 'myApp/add_menu_burgerking.html', {'form': form})


#Chowking-----------------------------------------------------------------------------------------------
def edit_menu_chowking(request, menu_id):
    menu_item = get_object_or_404(Menu, pk=menu_id)
    
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('Chowking')
    else:
        form = MenuForm(instance=menu_item)
    
    return render(request, "myApp/edit_menu_chowking.html", {'form': form, 'menu_item': menu_item})

def delete_menu_chowking(request, menu_id):
    menu_item = get_object_or_404(Menu, pk=menu_id)
    menu_item.delete()
    return redirect('Chowking')

def add_menu_chowking(request):
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.restaurant_name2 = "Chowking"
            menu_item.save()
            return redirect('Chowking')
    else:
        form = MenuForm()
    
    return render(request, 'myApp/add_menu_chowking.html', {'form': form})


#MangInasal-----------------------------------------------------------------------------------------------
def edit_menu_manginasal(request, menu_id):
    menu_item = get_object_or_404(Menu, pk=menu_id)
    
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('MangInasal')
    else:
        form = MenuForm(instance=menu_item)
    
    return render(request, "myApp/edit_menu_manginasal.html", {'form': form, 'menu_item': menu_item})

def delete_menu_manginasal(request, menu_id):
    menu_item = get_object_or_404(Menu, pk=menu_id)
    menu_item.delete()
    return redirect('MangInasal')

def add_menu_manginasal(request):
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.restaurant_name2 = "MangInasal"
            menu_item.save()
            return redirect('MangInasal')
    else:
        form = MenuForm()
    
    return render(request, 'myApp/add_menu_manginasal.html', {'form': form})


#PizzaHut-----------------------------------------------------------------------------------------------
def edit_menu_pizzahut(request, menu_id):
    menu_item = get_object_or_404(Menu, pk=menu_id)
    
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('PizzaHut')
    else:
        form = MenuForm(instance=menu_item)
    
    return render(request, "myApp/edit_menu_pizzahut.html", {'form': form, 'menu_item': menu_item})

def delete_menu_pizzahut(request, menu_id):
    menu_item = get_object_or_404(Menu, pk=menu_id)
    menu_item.delete()
    return redirect('PizzaHut')

def add_menu_pizzahut(request):
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.restaurant_name2 = "PizzaHut"
            menu_item.save()
            return redirect('PizzaHut')
    else:
        form = MenuForm()
    
    return render(request, 'myApp/add_menu_pizzahut.html', {'form': form})
    

#Greenwich-----------------------------------------------------------------------------------------------
def edit_menu_greenwich(request, menu_id):
    menu_item = get_object_or_404(Menu, pk=menu_id)
    
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('Greenwich')
    else:
        form = MenuForm(instance=menu_item)
    
    return render(request, "myApp/edit_menu_greenwich.html", {'form': form, 'menu_item': menu_item})

def delete_menu_greenwich(request, menu_id):
    menu_item = get_object_or_404(Menu, pk=menu_id)
    menu_item.delete()
    return redirect('Greenwich')

def add_menu_greenwich(request):
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.restaurant_name2 = "Greenwich"
            menu_item.save()
            return redirect('Greenwich')
    else:
        form = MenuForm()
    
    return render(request, 'myApp/add_menu_greenwich.html', {'form': form})

def add_to_checkout(request, order_id):
    if request.method == 'POST':
        try:
            # Check if user is logged in
            if 'customer_id' not in request.session:
                messages.error(request, 'Please log in first!')
                return redirect('Orders')
            
            # Get the order and customer ID
            order = Orders.objects.get(order_id=order_id)
            customer_id = request.session['customer_id']
            
            # Create new checkout item
            checkout_item = Checkout(
                checkout_name=order.order_name,
                checkout_description=order.order_description,
                checkout_price=order.order_price,
                checkout_image=order.orders_image,
                checkout_customer=customer_id  # Use logged-in customer's ID
            )
            checkout_item.save()
            
            # Delete the order
            order.delete()
            
            messages.success(request, 'Item added to checkout successfully!')
            return redirect('Orders')
            
        except Orders.DoesNotExist:
            messages.error(request, 'Order not found!')
            return redirect('Orders')
    
    return redirect('Orders')

def remove_from_checkout(request, checkout_id):
    if request.method == 'POST':
        try:
            # Get the checkout item and verify it belongs to the logged-in customer
            if 'customer_id' in request.session:
                checkout_item = Checkout.objects.get(
                    checkout_id=checkout_id,
                    checkout_customer=request.session['customer_id']
                )
                checkout_item.delete()
                messages.success(request, 'Item removed from checkout successfully!')
            else:
                messages.error(request, 'Please log in first!')
        except Checkout.DoesNotExist:
            messages.error(request, 'Item not found in checkout!')
    
    return redirect('Checkout')

def complete_order(request):
    if request.method == 'POST':
        try:
            if 'customer_id' in request.session:
                # Delete all checkout items for the logged-in customer
                Checkout.objects.filter(checkout_customer=request.session['customer_id']).delete()
                messages.success(request, 'Order completed successfully!')
            else:
                messages.error(request, 'Please log in first!')
        except Exception as e:
            messages.error(request, 'An error occurred while completing your order.')
    
    return redirect('Checkout')

def add_driver(request):
    if request.method == 'POST':
        try:
            driver = Delivery_Driver(
                driver_fname=request.POST['driver_fname'],
                driver_lname=request.POST['driver_lname'],
                driver_phone_number=request.POST['driver_phone_number'],
                vehicle_type=request.POST['vehicle_type'],
                license_plate=request.POST['license_plate']
            )
            
            # Only set driver_image if a file was actually uploaded
            if request.FILES and 'driver_image' in request.FILES:
                driver.driver_image = request.FILES['driver_image']
            
            driver.save()
            messages.success(request, 'Driver added successfully!')
            return redirect('Drivers')
        except Exception as e:
            messages.error(request, f'Error adding driver: {str(e)}')
            return redirect('Drivers')
    
    return redirect('Drivers')

def edit_driver(request, driver_id):
    if request.method == 'POST':
        try:
            driver = Delivery_Driver.objects.get(driver_id=driver_id)
            driver.driver_fname = request.POST['driver_fname']
            driver.driver_lname = request.POST['driver_lname']
            driver.driver_phone_number = request.POST['driver_phone_number']
            driver.vehicle_type = request.POST['vehicle_type']
            driver.license_plate = request.POST['license_plate']
            
            if request.FILES and 'driver_image' in request.FILES:
                driver.driver_image = request.FILES['driver_image']
            
            driver.save()
            messages.success(request, 'Driver updated successfully!')
            return redirect('Drivers')
        except Exception as e:
            messages.error(request, f'Error updating driver: {str(e)}')
            return redirect('Drivers')
    
    return redirect('Drivers')

def remove_driver(request, driver_id):
    try:
        driver = Delivery_Driver.objects.get(driver_id=driver_id)
        # Delete the driver's image if it exists
        if driver.driver_image:
            if os.path.isfile(driver.driver_image.path):
                os.remove(driver.driver_image.path)
        driver.delete()
        messages.success(request, 'Driver has been successfully removed.')
    except Delivery_Driver.DoesNotExist:
        messages.error(request, 'Driver not found.')
    except Exception as e:
        messages.error(request, f'Error removing driver: {str(e)}')
    
    return redirect('Drivers')

def delete_account(request):
    if 'customer_id' not in request.session:
        messages.error(request, 'You must be logged in to delete your account.')
        return redirect('login')
    
    try:
        customer = Customer.objects.get(customer_id=request.session['customer_id'])
        
        # Delete associated orders and checkouts
        Orders.objects.filter(order_customer=customer.customer_id).delete()
        Checkout.objects.filter(checkout_customer=customer.customer_id).delete()
        
        # Delete the customer
        customer.delete()
        
        # Logout and clear session
        auth_logout(request)
        request.session.pop('customer_id', None)
        
        messages.success(request, 'Your account has been successfully deleted.')
        return redirect('login')
    
    except Customer.DoesNotExist:
        messages.error(request, 'Account not found.')
        return redirect('login') 
        # Delete associated orders and checkouts
        Orders.objects.filter(order_customer=customer.customer_id).delete()
        Checkout.objects.filter(checkout_customer=customer.customer_id).delete()
        
        # Delete the customer
        customer.delete()
        
        # Logout and clear session
        auth_logout(request)
        request.session.pop('customer_id', None)
        
        messages.success(request, 'Your account has been successfully deleted.')
        return redirect('login')
    
    except Customer.DoesNotExist:
        messages.error(request, 'Account not found.')
        return redirect('login')

def edit_profile(request):
    if request.method == 'POST':
        if 'customer_id' not in request.session:
            messages.error(request, 'You must be logged in to edit your profile.')
            return redirect('login')

        try:
            customer = Customer.objects.get(customer_id=request.session['customer_id'])
            
            # Update customer details
            customer.first_name = request.POST.get('first_name')
            customer.last_name = request.POST.get('last_name')
            customer.email = request.POST.get('email')
            customer.phone_number = request.POST.get('phone_number')
            customer.address = request.POST.get('address')
            
            # Handle profile image upload
            if 'customer_image' in request.FILES:
                customer.customer_image = request.FILES['customer_image']
            
            customer.save()
            
            messages.success(request, 'Profile updated successfully!')
            return redirect('Profile')
        
        except Customer.DoesNotExist:
            messages.error(request, 'Customer not found.')
            return redirect('login')
    
    # If not a POST request, redirect to profile
    return redirect('Profile')