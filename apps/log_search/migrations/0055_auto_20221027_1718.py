# Generated by Django 3.2.15 on 2022-10-27 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("log_search", "0054_favorite_is_enable_display_fields"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="favorite",
            unique_together={("name", "space_uid", "index_set_id", "created_by")},
        ),
        migrations.AlterUniqueTogether(
            name="favoritegroup",
            unique_together={("name", "space_uid", "created_by")},
        ),
    ]
