# Generated by Django 2.2.4 on 2020-02-21 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '__first__'),
        ('post', '0004_auto_20200221_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='query_city_tag',
            field=models.ManyToManyField(to='people.City'),
        ),
        migrations.AddField(
            model_name='query',
            name='query_country_tag',
            field=models.ManyToManyField(to='people.Country'),
        ),
        migrations.AddField(
            model_name='query',
            name='query_school_tag',
            field=models.ManyToManyField(to='people.School'),
        ),
    ]
