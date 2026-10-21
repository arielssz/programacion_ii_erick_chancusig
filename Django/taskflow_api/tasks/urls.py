from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("about-me", views.about_me, name="about_me"),
    path("greeting/<str:nombre>", views.greeting, name="greeting"),
    path("home", views.home, name="home"),
    
]