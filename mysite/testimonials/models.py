from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model_string
from wagtail.models import Page
from wagtail.snippets.models import register_snippet


@register_snippet
class Testimonial(models.Model):
    RATING_CHOICES = [
        (1, "⭐"),
        (2, "⭐⭐"),
        (3, "⭐⭐⭐"),
        (4, "⭐⭐⭐⭐"),
        (5, "⭐⭐⭐⭐⭐"),
    ]

    name = models.CharField(
        max_length=100,
        verbose_name="Client Name"
    )

    company = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Company"
    )

    position = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Position"
    )

    email = models.EmailField(
        blank=True
    )

    photo = models.ForeignKey(
        get_image_model_string(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+"
    )

    project_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Project Name"
    )

    website = models.URLField(
        blank=True,
        verbose_name="Website"
    )

    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        default=5
    )

    testimonial = models.TextField(
        verbose_name="Testimonial"
    )

    featured = models.BooleanField(
        default=False,
        help_text="Display this testimonial in the featured section."
    )

    published = models.BooleanField(
        default=False,
        help_text="Display this testimonial on the website."
    )

    consent_to_publish = models.BooleanField(
        default=False,
        verbose_name="Consent to Publish",
        help_text="Client has given permission to publish this testimonial."
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("company"),
        FieldPanel("position"),
        FieldPanel("email"),
        FieldPanel("photo"),
        FieldPanel("project_name"),
        FieldPanel("website"),
        FieldPanel("rating"),
        FieldPanel("testimonial"),
        FieldPanel("consent_to_publish"),
        FieldPanel("featured"),
        FieldPanel("published"),
    ]

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        if self.company:
            return f"{self.name} ({self.company})"
        return self.name


class TestimonialsPage(Page):
    hero_title = models.CharField(
        max_length=255,
        default="What Our Clients Say"
    )

    hero_description = models.TextField(
        blank=True,
        help_text="Short description displayed below the hero title."
    )

    cta_title = models.CharField(
        max_length=255,
        blank=True,
        default="Share Your Experience"
    )

    cta_description = models.TextField(
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("hero_description"),
        FieldPanel("cta_title"),
        FieldPanel("cta_description"),
    ]

    def get_context(self, request):
        context = super().get_context(request)

        context["featured_testimonial"] = (
            Testimonial.objects.filter(
                published=True,
                featured=True,
            ).first()
        )

        context["testimonials"] = (
            Testimonial.objects.filter(
                published=True
            ).order_by("-created_at")
        )

        return context

    class Meta:
        verbose_name = "Testimonials Page"