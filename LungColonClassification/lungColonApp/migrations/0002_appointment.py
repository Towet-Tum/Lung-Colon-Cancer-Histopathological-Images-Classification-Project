# Generated by Django 5.0.1 on 2024-02-03 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lungColonApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Appointment",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=150)),
                ("message", models.TextField()),
                ("appointment_date", models.DateField()),
                ("is_booked", models.BooleanField(default=False)),
            ],
        ),
    ]
