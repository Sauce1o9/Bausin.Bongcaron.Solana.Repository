from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth import authenticate, login # type: ignore
from django.contrib import messages # type: ignore
from .forms import LoginForm, SignupForm
from myApp import views

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

def browse(request):
    return render(request, "myApp/browse.html")

def restaurants(request):
    return render(request, "myApp/restaurants.html")
