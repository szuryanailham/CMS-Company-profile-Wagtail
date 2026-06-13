from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    hero_label = models.CharField(
        max_length=100,
        blank=True,
        default="FOR LEARNERS"
    )

    hero_title = models.CharField(
        max_length=255,
        blank=True,
        default=""
    )

    hero_subtitle = models.TextField(
        blank=True,
        default=""
    )

    hero_primary_button_text = models.CharField(
        max_length=100,
        blank=True,
        default="START BUILDING FREE"
    )

    hero_primary_button_url = models.URLField(
        blank=True
    )

    hero_secondary_button_text = models.CharField(
        max_length=100,
        blank=True,
        default="BROWSE CHALLENGES"
    )

    hero_secondary_button_url = models.URLField(
        blank=True
    )

    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero_label"),
        FieldPanel("hero_title"),
        FieldPanel("hero_subtitle"),
        FieldPanel("hero_primary_button_text"),
        FieldPanel("hero_primary_button_url"),
        FieldPanel("hero_secondary_button_text"),
        FieldPanel("hero_secondary_button_url"),
        FieldPanel("hero_image"),
    ]