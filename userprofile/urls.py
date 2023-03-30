from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.login_user, name="login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("profile", views.profile, name="profile"),
    path("map", views.map, name="map"),
    path("signup", views.signup, name="signup"),
    
]
