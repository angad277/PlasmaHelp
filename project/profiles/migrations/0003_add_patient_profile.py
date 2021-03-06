# Generated by Django 3.0.7 on 2020-06-16 09:52

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0009_add_patient_profile"),
        ("profiles", "0002_made_blank_false"),
    ]

    operations = [
        migrations.CreateModel(
            name="PatientProfile",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=30, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=150, verbose_name="Last Name"),
                ),
                ("is_complete", models.BooleanField(default=False)),
                (
                    "location",
                    django.contrib.gis.db.models.fields.PointField(
                        srid=4326,
                        verbose_name="Your Location (It will be kept confidential)",
                    ),
                ),
                ("birth_date", models.DateField(verbose_name="Date of Birth")),
                (
                    "mobile_number",
                    models.CharField(
                        blank=True,
                        help_text="Format (+91xxxxxxxxxx)",
                        max_length=15,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+91xxxxxxxxxx'. Up to 9-10 digits allowed.",
                                regex="^\\+?91?\\d{9,10}$",
                            )
                        ],
                        verbose_name="Contact Number",
                    ),
                ),
            ],
        ),
    ]
