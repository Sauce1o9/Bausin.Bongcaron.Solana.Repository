from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth import authenticate, login # type: ignore
from django.contrib import messages # type: ignore
from .forms import LoginForm, SignupForm, MenuForm
from .models import Orders, Customer, Restaurant, Delivery_Driver, Menu
from django.http import Http404  # Add this import


# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        print(f"Username: {username}, Email: {email}, Password: {password}, Confirm: {password_confirm}")
        
        if password and password == password_confirm:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match or were not provided')
    return render(request, "myApp/signup.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
       
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, "myApp/login.html")  
















def home(request):
    return render(request, "myApp/home.html")

def restaurants(request):
    return render(request, "myApp/restaurants.html")

def McDonalds(request):
    menu_items = Menu.objects.filter(restaurant_name2="McDonalds")
    context = {'menu_items': menu_items}
    return render(request, "myApp/McDonalds.html", context)

def Jollibee(request):
    menu_items = Menu.objects.filter(restaurant_name2="Jollibee")
    context = {'menu_items': menu_items}
    return render(request, "myApp/Jollibee.html", context)

def KFC(request):
    menu_items = Menu.objects.filter(restaurant_name2="KFC")
    context = {'menu_items': menu_items}
    return render(request, "myApp/KFC.html", context)

def BurgerKing(request):
    menu_items = Menu.objects.filter(restaurant_name2="BurgerKing")
    context = {'menu_items': menu_items}
    return render(request, "myApp/BurgerKing.html", context)

def Chowking(request):
    menu_items = Menu.objects.filter(restaurant_name2="Chowking")
    context = {'menu_items': menu_items}
    return render(request, "myApp/Chowking.html", context)

def Greenwich(request):
    menu_items = Menu.objects.filter(restaurant_name2="McDoGreenwichnalds")
    context = {'menu_items': menu_items}
    return render(request, "myApp/Greenwich.html", context)

def MangInasal(request):
    menu_items = Menu.objects.filter(restaurant_name2="MangInasal")
    context = {'menu_items': menu_items}
    return render(request, "myApp/MangInasal.html", context)

def PizzaHut(request):
    menu_items = Menu.objects.filter(restaurant_name2="PizzaHut")
    context = {'menu_items': menu_items}
    return render(request, "myApp/PizzaHut.html", context)

def edit_menu(request, menu_id):
    menu_item = get_object_or_404(Menu, pk=menu_id)
    
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('McDonalds')  # Redirect to the McDonald's page after saving
    else:
        form = MenuForm(instance=menu_item)
    
    return render(request, "myApp/edit_menu.html", {'form': form, 'menu_item': menu_item})

def delete_menu(request, menu_id):
    menu_item = get_object_or_404(Menu, pk=menu_id)
    menu_item.delete()  # Delete the menu item
    return redirect('McDonalds')  # Redirect to the McDonald's page after deletion

def add_menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.restaurant_name2 = "McDonalds"
            menu_item.save()
            return redirect('McDonalds')
    else:
        form = MenuForm()
    
    return render(request, 'myApp/add_menu.html', {'form': form})