# Generated by Django 5.1 on 2024-08-30 15:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0007_habit_date_start"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="date_start",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Дата начала"
            ),
        ),
    ]
