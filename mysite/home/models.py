from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    TabbedInterface,
    ObjectList,
)


class ShowcaseItem(Orderable):
    page = ParentalKey(
        'home.HomePage',
        on_delete=models.CASCADE,
        related_name='showcase_items',
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    image_alt = models.CharField(max_length=200, blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('image'),
        FieldPanel('image_alt'),
    ]


class ServicePackage(Orderable):
    page = ParentalKey(
        'home.HomePage',
        on_delete=models.CASCADE,
        related_name='service_packages',
    )
    name = models.CharField(max_length=200)
    price = models.CharField(
        max_length=100,
        help_text='Contoh: $999/mo atau Rp 5.000.000',
    )
    description = models.TextField()
    is_popular = models.BooleanField(default=False)
    features_text = models.TextField(
        help_text='Satu fitur per baris',
        blank=True,
    )
    button_text = models.CharField(max_length=100, default='Get Started')
    button_url = models.URLField(blank=True)

    @property
    def features_list(self):
        return [f.strip() for f in self.features_text.splitlines() if f.strip()]

    panels = [
        FieldPanel('name'),
        FieldPanel('price'),
        FieldPanel('description'),
        FieldPanel('is_popular'),
        FieldPanel('features_text'),
        FieldPanel('button_text'),
        FieldPanel('button_url'),
    ]


class ClientLogo(Orderable):
    page = ParentalKey(
        'home.HomePage',
        on_delete=models.CASCADE,
        related_name='client_logos',
    )
    company_name = models.CharField(max_length=200)
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    website_url = models.URLField(blank=True)

    panels = [
        FieldPanel('company_name'),
        FieldPanel('logo'),
        FieldPanel('website_url'),
    ]


class HomePageVideoStat(Orderable):
    page = ParentalKey(
        'home.HomePage',
        on_delete=models.CASCADE,
        related_name='video_stats',
    )
    value = models.CharField(
        max_length=20,
        help_text='Example: 10+, 500+, 24/7',
    )
    label = models.CharField(
        max_length=100,
        help_text='Example: Years of Experience',
    )

    panels = [
        FieldPanel('value'),
        FieldPanel('label'),
    ]


class HomePage(Page):

    # --- Hero Section ---
    hero_label = models.CharField(
        max_length=100,
        blank=True,
        default='FOR LEARNERS',
    )
    hero_title = models.CharField(
        max_length=255,
        blank=True,
        default='',
    )
    hero_subtitle = models.TextField(
        blank=True,
        default='',
    )
    hero_primary_button_text = models.CharField(
        max_length=100,
        blank=True,
        default='START BUILDING FREE',
    )
    hero_primary_button_url = models.URLField(blank=True)
    hero_secondary_button_text = models.CharField(
        max_length=100,
        blank=True,
        default='BROWSE CHALLENGES',
    )
    hero_secondary_button_url = models.URLField(blank=True)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    # --- Showcase Section ---
    showcase_label = models.CharField(
        max_length=100,
        blank=True,
        default='OUR SERVICES',
    )
    showcase_title = models.CharField(
        max_length=255,
        blank=True,
        default='',
    )
    showcase_subtitle = models.TextField(
        blank=True,
        default='',
    )

    # --- Service Packages Section ---
    packages_label = models.CharField(
        max_length=100,
        blank=True,
        default='OUR SERVICES',
    )
    packages_title = models.CharField(
        max_length=255,
        blank=True,
        default='',
    )
    packages_subtitle = models.TextField(
        blank=True,
        default='',
    )

    # --- Clients Marquee Section ---
    clients_marquee_title = models.CharField(
        max_length=255,
        blank=True,
        default='Trusted by Leading Companies',
    )
    clients_marquee_subtitle = models.TextField(
        blank=True,
        default='',
    )

    # --- Testimonials Section ---
    testimonials_label = models.CharField(
        max_length=100,
        blank=True,
        default='TESTIMONIALS',
    )
    testimonials_title = models.CharField(
        max_length=255,
        blank=True,
        default='What Our Clients Say',
    )
    testimonials_subtitle = models.TextField(
        blank=True,
        default='Hear from businesses and organizations that have trusted us to bring their ideas to life.',
    )
    testimonials_stat_1_value = models.CharField(
        max_length=20,
        blank=True,
        default='500+',
    )
    testimonials_stat_1_label = models.CharField(
        max_length=100,
        blank=True,
        default='Happy Clients',
    )
    testimonials_stat_2_value = models.CharField(
        max_length=20,
        blank=True,
        default='98%',
    )
    testimonials_stat_2_label = models.CharField(
        max_length=100,
        blank=True,
        default='Client Satisfaction',
    )
    testimonials_stat_3_value = models.CharField(
        max_length=20,
        blank=True,
        default='150+',
    )
    testimonials_stat_3_label = models.CharField(
        max_length=100,
        blank=True,
        default='Projects Delivered',
    )
    testimonials_stat_4_value = models.CharField(
        max_length=20,
        blank=True,
        default='50+',
    )
    testimonials_stat_4_label = models.CharField(
        max_length=100,
        blank=True,
        default='Long-Term Partnerships',
    )

    # --- Video Section ---
    video_section_label = models.CharField(
        max_length=100,
        blank=True,
        default='WATCH & LEARN',
    )
    video_section_title = models.CharField(
        max_length=255,
        blank=True,
        default='',
    )
    video_section_subtitle = models.TextField(
        blank=True,
        default='',
    )
    video_embed_url = models.URLField(
        blank=True,
        help_text='YouTube embed URL, example: https://www.youtube.com/embed/xxx',
    )

    # --- Admin Panels ---
    hero_panels = [
        MultiFieldPanel([
            FieldPanel('hero_label'),
            FieldPanel('hero_title'),
            FieldPanel('hero_subtitle'),
        ], heading='Hero Text'),
        MultiFieldPanel([
            FieldPanel('hero_primary_button_text'),
            FieldPanel('hero_primary_button_url'),
            FieldPanel('hero_secondary_button_text'),
            FieldPanel('hero_secondary_button_url'),
        ], heading='Call to Action Buttons'),
        FieldPanel('hero_image'),
    ]

    video_panels = [
        MultiFieldPanel([
            FieldPanel('video_section_label'),
            FieldPanel('video_section_title'),
            FieldPanel('video_section_subtitle'),
            FieldPanel('video_embed_url'),
        ], heading='Video Content'),
        InlinePanel('video_stats', label='Statistic Cards', min_num=0, max_num=6),
    ]

    showcase_panels = [
        MultiFieldPanel([
            FieldPanel('showcase_label'),
            FieldPanel('showcase_title'),
            FieldPanel('showcase_subtitle'),
        ], heading='Section Header'),
        InlinePanel('showcase_items', label='Showcase Items', min_num=0, max_num=10),
    ]

    packages_panels = [
        MultiFieldPanel([
            FieldPanel('packages_label'),
            FieldPanel('packages_title'),
            FieldPanel('packages_subtitle'),
        ], heading='Section Header'),
        InlinePanel('service_packages', label='Service Packages', min_num=0, max_num=8),
    ]

    clients_panels = [
        MultiFieldPanel([
            FieldPanel('clients_marquee_title'),
            FieldPanel('clients_marquee_subtitle'),
        ], heading='Section Header'),
        InlinePanel('client_logos', label='Client Logos'),
    ]

    testimonials_panels = [
        MultiFieldPanel([
            FieldPanel('testimonials_label'),
            FieldPanel('testimonials_title'),
            FieldPanel('testimonials_subtitle'),
        ], heading='Section Header'),
        MultiFieldPanel([
            FieldPanel('testimonials_stat_1_value'),
            FieldPanel('testimonials_stat_1_label'),
            FieldPanel('testimonials_stat_2_value'),
            FieldPanel('testimonials_stat_2_label'),
            FieldPanel('testimonials_stat_3_value'),
            FieldPanel('testimonials_stat_3_label'),
            FieldPanel('testimonials_stat_4_value'),
            FieldPanel('testimonials_stat_4_label'),
        ], heading='Statistics (Optional — leave blank to hide)'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading='Page Settings'),
        ObjectList(hero_panels, heading='Hero Section'),
        ObjectList(showcase_panels, heading='Showcase Section'),
        ObjectList(video_panels, heading='Video Section'),
        ObjectList(clients_panels, heading='Client Logos'),
        ObjectList(packages_panels, heading='Service Packages'),
        ObjectList(testimonials_panels, heading='Testimonials'),
        ObjectList(Page.promote_panels, heading='SEO & Promote'),
    ])

    def get_context(self, request):
        context = super().get_context(request)
        from testimonials.models import Testimonial
        from question_and_answer.models import QuestionAndAnswer

        context['featured_testimonials'] = list(
            Testimonial.objects
            .filter(status='approved', is_featured=True)
            .order_by('display_order')[:5]
        )
        context['home_faqs'] = list(
            QuestionAndAnswer.objects
            .filter(status='approved', show_on_home=True)
            .order_by('-featured', 'display_order', '-created_at')[:8]
        )
        return context
