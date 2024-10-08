from django.shortcuts import render
from .models import MenuItem

def home(request):
    menu= MenuItem.objects.all()
    return render(request, 'base.html' ,{'menu': menu})

def menu(request):
    menu= MenuItem.objects.all()
    return render(request, 'menu_app/menu.html' ,{'menu': menu})

