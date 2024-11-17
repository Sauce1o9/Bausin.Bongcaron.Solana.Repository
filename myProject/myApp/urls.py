from . import views
from django.urls import path # type: ignore

urlpatterns = [
    path("", views.home, name="home"),
    path("restaurants", views.restaurants, name="restaurants"),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('browse/', views.browse, name='browse')
]
