from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
        ('wagtailimages', '0027_image_description'),
    ]

    operations = [

        # --- services_servicepage: tambah kolom yang belum ada ---

        migrations.RunSQL(
            sql="ALTER TABLE services_servicepage ADD COLUMN hero_title varchar(200) NOT NULL DEFAULT ''",
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.RunSQL(
            sql="ALTER TABLE services_servicepage ADD COLUMN hero_subtitle varchar(255) NOT NULL DEFAULT ''",
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.RunSQL(
            sql="ALTER TABLE services_servicepage ADD COLUMN hero_description text NOT NULL DEFAULT ''",
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.RunSQL(
            sql="ALTER TABLE services_servicepage ADD COLUMN hero_image_id integer NULL REFERENCES wagtailimages_image(id)",
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.RunSQL(
            sql="ALTER TABLE services_servicepage ADD COLUMN cta_title varchar(200) NOT NULL DEFAULT ''",
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.RunSQL(
            sql="ALTER TABLE services_servicepage ADD COLUMN cta_description text NOT NULL DEFAULT ''",
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.RunSQL(
            sql="ALTER TABLE services_servicepage ADD COLUMN cta_button_text varchar(100) NOT NULL DEFAULT ''",
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.RunSQL(
            sql="ALTER TABLE services_servicepage ADD COLUMN cta_button_link varchar(255) NOT NULL DEFAULT ''",
            reverse_sql=migrations.RunSQL.noop,
        ),

        # --- services_serviceshowcase: buat tabel baru ---

        migrations.RunSQL(
            sql="""
                CREATE TABLE IF NOT EXISTS services_serviceshowcase (
                    id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                    sort_order integer NULL,
                    title varchar(200) NOT NULL DEFAULT '',
                    subtitle varchar(255) NOT NULL DEFAULT '',
                    description text NOT NULL DEFAULT '',
                    button_text varchar(100) NOT NULL DEFAULT '',
                    button_link varchar(255) NOT NULL DEFAULT '',
                    image_id integer NULL REFERENCES wagtailimages_image(id),
                    page_id integer NOT NULL REFERENCES services_servicepage(page_ptr_id)
                )
            """,
            reverse_sql="DROP TABLE IF EXISTS services_serviceshowcase",
        ),

        # --- services_serviceshowcasevalue: buat tabel baru ---

        migrations.RunSQL(
            sql="""
                CREATE TABLE IF NOT EXISTS services_serviceshowcasevalue (
                    id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                    sort_order integer NULL,
                    title varchar(200) NOT NULL DEFAULT '',
                    description varchar(500) NOT NULL DEFAULT '',
                    showcase_id integer NOT NULL REFERENCES services_serviceshowcase(id)
                )
            """,
            reverse_sql="DROP TABLE IF EXISTS services_serviceshowcasevalue",
        ),
    ]
