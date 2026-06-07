from .models import MenuItem

def navigation_menu(request):
    return {
        "menu_items": MenuItem.objects.filter(parent__isnull=True).prefetch_related("children")
    }