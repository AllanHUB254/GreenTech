from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def services(request):
    return render(request, "services.html")

def blogs(request):
    return render(request, "blogs.html")    

