from django.shortcuts import render

# Create your views here.


def index(request):
    """Home page for the Project"""
    return render(request, './main_app/home.html')


def log_in(request):
    """Log in page"""
    return render(request, './main_app/log_in.html')


def register(request):
    """Log in page"""
    return render(request, './main_app/register.html')
