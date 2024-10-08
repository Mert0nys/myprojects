from django.urls import path
from menu_app.views import menu,home

urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
]