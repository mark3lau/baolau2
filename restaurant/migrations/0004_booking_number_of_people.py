# Generated by Django 3.2.17 on 2023-02-21 21:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20230221_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='number_of_people',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
