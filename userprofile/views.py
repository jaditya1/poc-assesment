from django.shortcuts import render

# Create your views here.


def login_user(request):
    return render(request, "login.html")


def dashboard(request):
    return render(request, "dashboard.html")


def profile(request):
    return render(request, "profile.html")
