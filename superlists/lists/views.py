from django.shortcuts import render


# Create your views here.

def home_page(requests):
    # first view
    return render(requests, 'lists/home.html')
