# Generated by Django 5.2.2 on 2025-06-26 16:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_alter_basket_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='card_number',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxValueValidator(999)], verbose_name='Номер карты'),
        ),
    ]
