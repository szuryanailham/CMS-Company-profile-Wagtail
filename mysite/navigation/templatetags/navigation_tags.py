from django import template

from navigation.models import MenuItem

register = template.Library()


@register.simple_tag
def get_footer_menu_items():
    return MenuItem.objects.filter(parent=None).order_by("sort_order")
