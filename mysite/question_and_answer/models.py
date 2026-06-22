from django.core.paginator import Paginator
from django.db import models

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


STATUS_CHOICES = [
    ('pending', 'Pending Review'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
]


class QuestionAndAnswer(models.Model):
    question = models.TextField()
    answer = RichTextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
    )
    show_on_home = models.BooleanField(
        default=False,
        help_text='Display this approved question on the Home Page FAQ section',
    )
    featured = models.BooleanField(
        default=False,
        help_text='Featured questions appear before regular questions',
    )
    display_order = models.PositiveIntegerField(
        default=0,
        help_text='Lower number appears first',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    panels = [
        FieldPanel('question'),
        FieldPanel('answer'),
        MultiFieldPanel([
            FieldPanel('status'),
            FieldPanel('show_on_home'),
            FieldPanel('featured'),
            FieldPanel('display_order'),
        ], heading='Publishing Settings'),
    ]

    class Meta:
        ordering = ['-featured', 'display_order', '-created_at']
        verbose_name = 'Question and Answer'
        verbose_name_plural = 'Questions and Answers'

    def __str__(self):
        return f'{self.question[:80]} ({self.get_status_display()})'


class FAQPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    subpage_types = []
    parent_page_types = ['wagtailcore.Page', 'home.HomePage']

    def get_context(self, request):
        context = super().get_context(request)

        faqs = QuestionAndAnswer.objects.filter(status='approved')

        query = request.GET.get('q', '').strip()
        if query:
            faqs = faqs.filter(
                models.Q(question__icontains=query)
                | models.Q(answer__icontains=query)
            )

        faqs = faqs.order_by('-featured', 'display_order', '-created_at')
        paginator = Paginator(faqs, 10)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        context.update({
            'faqs': page_obj,
            'query': query,
            'total_count': paginator.count,
        })
        return context


class AskQuestionPage(Page):
    success_message = models.TextField(
        default=(
            'Thank you for your question! '
            'It is now pending review and may be published after our team approves it.'
        ),
    )

    content_panels = Page.content_panels + [
        FieldPanel('success_message'),
    ]

    subpage_types = []
    parent_page_types = ['wagtailcore.Page', 'home.HomePage']

    def serve(self, request):
        from django.shortcuts import redirect, render
        from question_and_answer.forms import QuestionSubmitForm

        if request.method == 'POST':
            form = QuestionSubmitForm(request.POST)
            if form.is_valid():
                QuestionAndAnswer.objects.create(
                    question=form.cleaned_data['question'],
                    answer='',
                    status='pending',
                    show_on_home=False,
                    featured=False,
                )
                return redirect(self.url + '?submitted=true')
        else:
            form = QuestionSubmitForm()

        context = self.get_context(request)
        context['form'] = form
        context['submitted'] = request.GET.get('submitted') == 'true'
        return render(request, self.get_template(request), context)
