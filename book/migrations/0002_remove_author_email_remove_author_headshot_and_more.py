# Generated by Django 4.2 on 2023-04-04 19:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="author",
            name="email",
        ),
        migrations.RemoveField(
            model_name="author",
            name="headshot",
        ),
        migrations.RemoveField(
            model_name="author",
            name="salutation",
        ),
    ]