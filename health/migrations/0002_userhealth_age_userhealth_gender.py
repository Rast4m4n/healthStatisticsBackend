# Generated by Django 4.1.3 on 2023-04-11 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("health", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userhealth",
            name="age",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="userhealth",
            name="gender",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
