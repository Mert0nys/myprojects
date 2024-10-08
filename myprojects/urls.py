from django.contrib import admin
from django.urls import path, include
from menu_app.views import menu, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("menu_app.urls")),
]
