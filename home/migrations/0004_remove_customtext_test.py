# Generated by Django 2.2.12 on 2020-06-03 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_customtext_test"),
    ]

    operations = [
        migrations.RemoveField(model_name="customtext", name="test",),
    ]
