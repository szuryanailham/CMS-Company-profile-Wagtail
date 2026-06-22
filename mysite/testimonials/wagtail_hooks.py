from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.snippets.models import register_snippet

from testimonials.models import Testimonial


class TestimonialViewSet(SnippetViewSet):
    model = Testimonial
    icon = 'pick'
    menu_label = 'Testimonials'
    menu_order = 300
    list_display = ['full_name', 'company', 'rating', 'is_featured', 'status', 'created_at']
    list_filter = ['status', 'is_featured', 'rating']
    search_fields = ['full_name', 'company', 'position', 'message']
    ordering = ['display_order', '-created_at']


register_snippet(TestimonialViewSet)
