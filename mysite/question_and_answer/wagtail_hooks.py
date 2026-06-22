from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from question_and_answer.models import QuestionAndAnswer


class QuestionAndAnswerViewSet(SnippetViewSet):
    model = QuestionAndAnswer
    icon = 'help'
    menu_label = 'Questions & Answers'
    menu_order = 310
    list_display = [
        'question',
        'status',
        'show_on_home',
        'featured',
        'display_order',
        'created_at',
    ]
    list_filter = ['status', 'show_on_home', 'featured']
    search_fields = ['question', 'answer']
    ordering = ['-featured', 'display_order', '-created_at']


register_snippet(QuestionAndAnswerViewSet)
