from . import views
from django.urls import path # type: ignore
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("Profile", views.Profile, name="Profile"),
    path("login/", views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    path("signup/", views.signup, name="signup"),
    path("Orders", views.orders_list, name="Orders"),
    path("Checkout", views.checkout_view, name="Checkout"),
    path("Drivers", views.Drivers, name="Drivers"),
    path("admin_page", views.admin_page, name="admin_page"),
    path("admin_menu", views.admin_menu, name="admin_menu"),
    path("admin_drivers", views.admin_drivers, name="admin_drivers"),
    path("admin_orders", views.admin_orders, name="admin_orders"),
    path("add_customer/", views.add_customer, name="add_customer"),
    path("edit_customer/<str:customer_id>/", views.edit_customer, name="edit_customer"),
    path("delete_customer/<str:customer_id>/", views.delete_customer, name="delete_customer"),
    path("McDonalds", views.McDonalds, name="McDonalds"),
    path("Jollibee", views.Jollibee, name="Jollibee"),
    path("KFC", views.KFC, name="KFC"),
    path("BurgerKing", views.BurgerKing, name="BurgerKing"),
    path("Chowking", views.Chowking, name="Chowking"),
    path("Greenwich", views.Greenwich, name="Greenwich"),
    path("MangInasal", views.MangInasal, name="MangInasal"),
    path("PizzaHut", views.PizzaHut, name="PizzaHut"),
    #McDonalds
    path('edit-menu/<int:menu_id>/', views.edit_menu, name='edit_menu'),
    path('delete-menu/<int:menu_id>/', views.delete_menu, name='delete_menu'),
    path('add-menu/', views.add_menu, name='add_menu'),
    #Jollibee
    path('edit-menu_jollibee/<int:menu_id>/', views.edit_menu_jollibee, name='edit_menu_jollibee'),
    path('delete-menu_jollibee/<int:menu_id>/', views.delete_menu_jollibee, name='delete_menu_jollibee'),
    path('add-menu_jollibee/', views.add_menu_jollibee, name='add_menu_jollibee'),
    #KFC
    path('edit-menu_kfc/<int:menu_id>/', views.edit_menu_kfc, name='edit_menu_kfc'),
    path('delete-menu_kfc/<int:menu_id>/', views.delete_menu_kfc, name='delete_menu_kfc'),
    path('add-menu_kfc/', views.add_menu_kfc, name='add_menu_kfc'),
    #BurgerKing
    path('edit-menu_burgerking/<int:menu_id>/', views.edit_menu_burgerking, name='edit_menu_burgerking'),
    path('delete-menu_burgerking/<int:menu_id>/', views.delete_menu_burgerking, name='delete_menu_burgerking'),
    path('add-menu_burgerking/', views.add_menu_burgerking, name='add_menu_burgerking'),
    #Chowking
    path('edit-menu_chowking/<int:menu_id>/', views.edit_menu_chowking, name='edit_menu_chowking'),
    path('delete-menu_chowking/<int:menu_id>/', views.delete_menu_chowking, name='delete_menu_chowking'),
    path('add-menu_chowking/', views.add_menu_chowking, name='add_menu_chowking'),
    #MangInasal
    path('edit-menu_manginasal/<int:menu_id>/', views.edit_menu_manginasal, name='edit_menu_manginasal'),
    path('delete-menu_manginasal/<int:menu_id>/', views.delete_menu_manginasal, name='delete_menu_manginasal'),
    path('add-menu_manginasal/', views.add_menu_manginasal, name='add_menu_manginasal'),
    #Drivers
    path('add-driver/', views.add_driver, name='add_driver'),
    path('edit-driver/<int:driver_id>/', views.edit_driver, name='edit_driver'),
    path('remove-driver/<int:driver_id>/', views.remove_driver, name='remove_driver'),
    #PizzaHut
    path('edit-menu_pizzahut/<int:menu_id>/', views.edit_menu_pizzahut, name='edit_menu_pizzahut'),
    path('delete-menu_pizzahut/<int:menu_id>/', views.delete_menu_pizzahut, name='delete_menu_pizzahut'),
    path('add-menu_pizzahut/', views.add_menu_pizzahut, name='add_menu_pizzahut'),
    #Greenwich
    path('edit-menu_greenwich/<int:menu_id>/', views.edit_menu_greenwich, name='edit_menu_greenwich'),
    path('delete-menu_greenwich/<int:menu_id>/', views.delete_menu_greenwich, name='delete_menu_greenwich'),
    path('add-menu_greenwich/', views.add_menu_greenwich, name='add_menu_greenwich'),
    path('add-to-checkout/<int:order_id>/', views.add_to_checkout, name='add_to_checkout'),
    path('remove-from-checkout/<int:checkout_id>/', views.remove_from_checkout, name='remove_from_checkout'),
    path('complete-order/', views.complete_order, name='complete_order'),
    path('add-order/', views.add_order, name='add_order'),
    path('delete-order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
