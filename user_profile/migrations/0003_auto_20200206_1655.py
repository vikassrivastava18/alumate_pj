# Generated by Django 2.2.3 on 2020-02-06 16:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20200206_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='school_end_year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2020), django.core.validators.MinValueValidator(1940)]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='school_start_year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2020), django.core.validators.MinValueValidator(1940)]),
        ),
    ]