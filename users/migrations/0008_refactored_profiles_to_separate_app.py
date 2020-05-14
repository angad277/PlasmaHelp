# Generated by Django 3.0.5 on 2020-05-03 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_modify_verbose_name"),
    ]

    operations = [
        migrations.RemoveField(model_name="hospitalprofile", name="user",),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                default=None, max_length=254, unique=True, verbose_name="email address"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_type",
            field=models.CharField(
                choices=[
                    ("DONOR", "Donor"),
                    ("HOSPITAL", "Hospital"),
                    ("STAFF", "Staff"),
                ],
                max_length=20,
            ),
        ),
        migrations.DeleteModel(name="DonorProfile",),
        migrations.DeleteModel(name="HospitalProfile",),
    ]