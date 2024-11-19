from . import views
from django.urls import path # type: ignore

urlpatterns = [
    path("", views.home, name="home"),
    path("restaurants", views.restaurant_menu, name="restaurants"),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path("McDonalds", views.restaurant_menu, name="McDonalds"),
    path("Jollibee", views.restaurant_menu, name="Jollibee"),
    path("KFC", views.restaurant_menu, name="KFC"),
    path("BurgerKing", views.restaurant_menu, name="BurgerKing"),
    path("Chowking", views.restaurant_menu, name="Chowking"),
    path("Greenwich", views.restaurant_menu, name="Greenwich"),
    path("MangInasal", views.restaurant_menu, name="MangInasal"),
    path("PizzaHut", views.restaurant_menu, name="PizzaHut"),
    
]
