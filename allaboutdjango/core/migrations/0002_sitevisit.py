# Generated by Django 5.2.4 on 2025-07-28 05:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SiteVisit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("region", models.CharField(blank=True, max_length=50, null=True)),
                ("inserted_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
