from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel



class HomePage(Page):
    hero_title = models.CharField(
        max_length=255,
        blank=True,
        default=""
    )

    hero_subtitle = models.TextField(
        blank=True,
        default=""
    )

    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("hero_subtitle"),
        FieldPanel("hero_image"),
    ]