# Generated by Django 5.1 on 2024-08-30 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0006_alter_habit_frequency"),
    ]

    operations = [
        migrations.AddField(
            model_name="habit",
            name="date_start",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 8, 30, 15, 55, 49, 496766, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Дата начала",
            ),
        ),
    ]
