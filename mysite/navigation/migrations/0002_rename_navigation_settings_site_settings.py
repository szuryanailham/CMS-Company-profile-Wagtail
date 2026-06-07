# Generated manually to preserve existing NavigationSettings data.

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("navigation", "0001_initial"),
        ("wagtailimages", "0027_image_description"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="NavigationSettings",
            new_name="SiteSettings",
        ),
        migrations.AddField(
            model_name="sitesettings",
            name="favicon",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
        migrations.AddField(
            model_name="sitesettings",
            name="email",
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name="sitesettings",
            name="phone",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="sitesettings",
            name="address",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="sitesettings",
            name="instagram",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="sitesettings",
            name="tiktok",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="sitesettings",
            name="youtube",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="sitesettings",
            name="whatsapp",
            field=models.URLField(
                blank=True,
                help_text="Use a full URL, for example https://wa.me/6281234567890",
            ),
        ),
    ]
