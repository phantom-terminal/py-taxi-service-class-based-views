# Generated by Django 4.0.3 on 2022-04-13 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0002_alter_driver_license_number"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="car",
            options={"ordering": ["model"]},
        ),
        migrations.AlterModelOptions(
            name="manufacturer",
            options={"ordering": ["name"]},
        ),
    ]
