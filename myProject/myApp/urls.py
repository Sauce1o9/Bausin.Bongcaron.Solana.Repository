from . import views
from django.urls import path # type: ignore

urlpatterns = [
    path("", views.home, name="home"),
    path("restaurants", views.restaurants, name="restaurants"),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path("McDonalds", views.McDonalds, name="McDonalds"),
    path("Jollibee", views.Jollibee, name="Jollibee"),
    path("KFC", views.KFC, name="KFC"),
    path("BurgerKing", views.BurgerKing, name="BurgerKing"),
    path("Chowking", views.Chowking, name="Chowking"),
    path("Greenwich", views.Greenwich, name="Greenwich"),
    path("MangInasal", views.MangInasal, name="MangInasal"),
    path("PizzaHut", views.PizzaHut, name="PizzaHut"),
    path('edit-menu/<int:menu_id>/', views.edit_menu, name='edit_menu'),
]

