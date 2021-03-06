# Generated by Django 4.0.5 on 2022-07-06 14:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_carmodel_auto_park'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9_\\s]{3,100}$', 'only a-z A-Z 0-9 _ space min 3 max 100')]),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(1000000)]),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1990), django.core.validators.MaxValueValidator(2022)]),
        ),
    ]
