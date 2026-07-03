from django.core.exceptions import PermissionDenied
from wagtail import hooks

@hooks.register("before_delete_page")
def prevent_homepage_delete(request, page):
    # Mencegah penghapusan HomePage
    if page.specific_class.__name__ == "HomePage":
        raise PermissionDenied("Home Page tidak boleh dihapus.")