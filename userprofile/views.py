from django.shortcuts import render

# Create your views here.


def login_user(request):
    return render(request, "login.html")


def dashboard(request):
    return render(request, "dashboard.html")


def profile(request):
    return render(request, "profile.html")


def map(request):
    return render(request, "map.html")


def signup(request):
    return render(request, "signup.html")
