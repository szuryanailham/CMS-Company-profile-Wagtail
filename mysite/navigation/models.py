from django.db import models

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.images import get_image_model_string
from wagtail.models import Page
from wagtail.snippets.models import register_snippet


# =========================
# MENU ITEM (SNIPPET)
# =========================
@register_snippet
class MenuItem(models.Model):
    title = models.CharField(max_length=100)

    page = models.ForeignKey(
        Page,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="+",
    )

    url = models.CharField(
        max_length=255,
        blank=True,
        help_text="Optional external URL",
    )

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="children",
    )

    sort_order = models.IntegerField(default=0)

    panels = [
        FieldPanel("title"),
        FieldPanel("page"),
        FieldPanel("url"),
        FieldPanel("parent"),
        FieldPanel("sort_order"),
    ]

    class Meta:
        ordering = ["sort_order"]

    def get_link(self):
        if self.page:
            return self.page.url
        return self.url

    def __str__(self):
        return self.title


# =========================
# SITE SETTINGS
# =========================
@register_setting
class SiteSettings(BaseSiteSetting):
    site_name = models.CharField(max_length=100, default="Company Blog")

    logo = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    favicon = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)

    company_description = models.TextField(blank=True)
    company_tagline = models.CharField(max_length=200, blank=True)

    instagram = models.URLField(blank=True)
    tiktok = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    whatsapp = models.URLField(
        blank=True,
        help_text="Use a full URL, for example https://wa.me/6281234567890",
    )
    facebook_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("site_name"),
                FieldPanel("logo"),
                FieldPanel("favicon"),
                FieldPanel("company_description"),
                FieldPanel("company_tagline"),
            ],
            heading="Branding",
        ),
        MultiFieldPanel(
            [
                FieldPanel("email"),
                FieldPanel("phone"),
                FieldPanel("address"),
            ],
            heading="Contact",
        ),
        MultiFieldPanel(
            [
                FieldPanel("instagram"),
                FieldPanel("tiktok"),
                FieldPanel("youtube"),
                FieldPanel("whatsapp"),
                FieldPanel("facebook_url"),
                FieldPanel("linkedin_url"),
                FieldPanel("twitter_url"),
            ],
            heading="Social links",
        ),
    ]
