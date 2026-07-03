from django.db import models

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
)
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel


class ServicePage(Page):
    """
    Landing page for all services.
    """

    # ==========================
    # HERO
    # ==========================

    hero_title = models.CharField(
        max_length=200,
    )

    hero_subtitle = models.CharField(
        max_length=255,
        blank=True,
    )

    hero_description = RichTextField(
        blank=True,
    )

    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    # ==========================
    # INTRODUCTION
    # ==========================

    introduction = RichTextField(blank=True)

    # ==========================
    # CTA
    # ==========================

    cta_title = models.CharField(
        max_length=200,
        blank=True,
    )

    cta_description = RichTextField(
        blank=True,
    )

    cta_button_text = models.CharField(
        max_length=100,
        blank=True,
    )

    cta_button_link = models.CharField(
        max_length=255,
        blank=True,
    )

    content_panels = Page.content_panels + [

        MultiFieldPanel(
            [
                FieldPanel("hero_title"),
                FieldPanel("hero_subtitle"),
                FieldPanel("hero_description"),
                FieldPanel("hero_image"),
            ],
            heading="Hero Section",
        ),

        MultiFieldPanel(
            [
                FieldPanel("introduction"),
            ],
            heading="Introduction",
        ),

        MultiFieldPanel(
            [
                InlinePanel(
                    "showcases",
                    label="Showcase",
                ),
            ],
            heading="Showcase Services",
        ),

        MultiFieldPanel(
            [
                FieldPanel("cta_title"),
                FieldPanel("cta_description"),
                FieldPanel("cta_button_text"),
                FieldPanel("cta_button_link"),
            ],
            heading="Call To Action",
        ),
    ]

class ServiceShowcase(Orderable, ClusterableModel):

    page = ParentalKey(
        "services.ServicePage",
        related_name="showcases",
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        max_length=200,
    )

    subtitle = models.CharField(
        max_length=255,
        blank=True,
    )

    description = RichTextField(
        blank=True,
    )

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    button_text = models.CharField(
        max_length=100,
        blank=True,
    )

    button_link = models.CharField(
        max_length=255,
        blank=True,
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("subtitle"),
        FieldPanel("description"),
        FieldPanel("image"),
        InlinePanel(
            "values",
            label="Values",
        ),
        FieldPanel("button_text"),
        FieldPanel("button_link"),
    ]


class ServiceShowcaseValue(Orderable):

    showcase = ParentalKey(
        "services.ServiceShowcase",
        related_name="values",
        on_delete=models.CASCADE,
    )

    title = models.CharField(max_length=200)

    description = models.CharField(
        max_length=500,
        blank=True,
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("description"),
    ]