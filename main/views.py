from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'title': 'Main Page',
    }
    return render(request, 'main/index.html', data)

def about(request):
    data = {
        'about': ' This is the about page',
    }
    return render(request, 'main/about.html', data)

def contact(request):
    data = {
        'contact': 'This is the contact page',
    }
    return render(request, 'main/contact.html', data)