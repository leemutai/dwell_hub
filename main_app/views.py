from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')


def properties(request):
    return None


def services(request):
    return None


def about(request):
    return None


def contact(request):
    return None

