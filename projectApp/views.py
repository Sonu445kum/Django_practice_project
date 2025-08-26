from django.shortcuts import render
from django.http import HttpResponse

# Home page view
def home(request):
    return render(request, "home.html")

# About page view
def about(request):
    return render(request, "about.html")

# Contact page view
def contact(request):
    return render(request, "contact.html")

# Your existing view for projectApp
def main_page(request):
    return render(request, "projectApp/main.html")
