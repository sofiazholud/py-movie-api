# Generated by Django 5.1.2 on 2024-10-30 21:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(help_text='Duration in minutes', validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
