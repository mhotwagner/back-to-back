# Generated by Django 2.0.2 on 2018-02-18 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_calculation_add_occurrences'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculation',
            name='last_occurrence',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
