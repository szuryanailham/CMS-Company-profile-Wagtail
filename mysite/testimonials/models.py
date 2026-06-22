from django.db import models
from django.core.paginator import Paginator

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


RATING_CHOICES = [
    (1, '1 - Poor'),
    (2, '2 - Fair'),
    (3, '3 - Good'),
    (4, '4 - Very Good'),
    (5, '5 - Excellent'),
]

STATUS_CHOICES = [
    ('pending', 'Pending Review'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
]


class Testimonial(models.Model):
    full_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200, blank=True)
    company = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    profile_photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Set by admin via Wagtail image chooser',
    )
    submitted_photo = models.ImageField(
        upload_to='testimonials/submitted/',
        null=True,
        blank=True,
        help_text='Photo uploaded via public submission form',
    )
    message = models.TextField()
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        null=True,
        blank=True,
    )
    is_featured = models.BooleanField(
        default=False,
        help_text='Mark to display on the Home Page testimonials section',
    )
    display_order = models.PositiveIntegerField(
        default=0,
        help_text='Lower number appears first',
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    panels = [
        MultiFieldPanel([
            FieldPanel('full_name'),
            FieldPanel('position'),
            FieldPanel('company'),
            FieldPanel('location'),
        ], heading='Author Info'),
        MultiFieldPanel([
            FieldPanel('profile_photo'),
            FieldPanel('submitted_photo'),
        ], heading='Profile Photo'),
        FieldPanel('message'),
        MultiFieldPanel([
            FieldPanel('rating'),
            FieldPanel('is_featured'),
            FieldPanel('display_order'),
            FieldPanel('status'),
        ], heading='Settings'),
    ]

    class Meta:
        ordering = ['display_order', '-created_at']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return f'{self.full_name} ({self.get_status_display()})'

    @property
    def display_position(self):
        parts = [p for p in [self.position, self.company] if p]
        return ' · '.join(parts)

    @property
    def avatar_initial(self):
        return self.full_name[0].upper() if self.full_name else '?'


class TestimonialsPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    subpage_types = []
    parent_page_types = ['wagtailcore.Page', 'home.HomePage']

    def get_context(self, request):
        context = super().get_context(request)

        testimonials = Testimonial.objects.filter(status='approved').order_by('display_order', '-created_at')

        query = request.GET.get('q', '').strip()
        if query:
            testimonials = testimonials.filter(
                models.Q(full_name__icontains=query)
                | models.Q(company__icontains=query)
                | models.Q(message__icontains=query)
            )

        rating_filter = request.GET.get('rating', '').strip()
        if rating_filter.isdigit() and 1 <= int(rating_filter) <= 5:
            testimonials = testimonials.filter(rating=int(rating_filter))

        paginator = Paginator(testimonials, 10)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        context.update({
            'testimonials': page_obj,
            'query': query,
            'rating_filter': rating_filter,
            'rating_choices': range(1, 6),
            'total_count': paginator.count,
        })
        return context


class SubmitTestimonialPage(Page):
    success_message = models.TextField(
        default=(
            'Terima kasih atas testimonial Anda! '
            'Testimonial Anda sedang dalam proses review dan akan segera ditampilkan setelah disetujui.'
        ),
    )

    content_panels = Page.content_panels + [
        FieldPanel('success_message'),
    ]

    subpage_types = []
    parent_page_types = ['wagtailcore.Page', 'home.HomePage']

    def serve(self, request):
        from django.shortcuts import render, redirect
        from testimonials.forms import TestimonialSubmitForm

        if request.method == 'POST':
            form = TestimonialSubmitForm(request.POST, request.FILES)
            if form.is_valid():
                rating_val = form.cleaned_data.get('rating')
                Testimonial.objects.create(
                    full_name=form.cleaned_data['full_name'],
                    position=form.cleaned_data.get('position', ''),
                    company=form.cleaned_data.get('company', ''),
                    location=form.cleaned_data.get('location', ''),
                    submitted_photo=form.cleaned_data.get('submitted_photo'),
                    rating=int(rating_val) if rating_val else None,
                    message=form.cleaned_data['message'],
                    status='pending',
                )
                return redirect(self.url + '?submitted=true')
        else:
            form = TestimonialSubmitForm()

        context = self.get_context(request)
        context['form'] = form
        context['submitted'] = request.GET.get('submitted') == 'true'
        return render(request, self.get_template(request), context)
