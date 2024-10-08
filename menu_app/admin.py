from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'parent', 'menu_name')
    list_filter = ('menu_name',)

admin.site.register(MenuItem, MenuItemAdmin)
