# Generated by Django 4.2.16 on 2025-01-15 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("razvert", "0004_randomuser_delete_question"),
    ]

    operations = [
        migrations.DeleteModel(
            name="WeatherRequest",
        ),
    ]
