from django import template
from menu_app.models import MenuItem
from django.urls import reverse

register = template.Library()

def build_menu(menu_name, parent=None):
    items = MenuItem.objects.filter(menu_name=menu_name, parent=parent).prefetch_related('children')
    return items

@register.inclusion_tag('menu_app/menu.html')
def draw_menu(menu_name):
    root_items = build_menu(menu_name, parent=None)
    return {'root_items': root_items, 'menu_name': menu_name}
