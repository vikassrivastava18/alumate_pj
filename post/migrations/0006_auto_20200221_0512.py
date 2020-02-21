# Generated by Django 2.2.4 on 2020-02-21 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20200221_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='query_city_tag',
            field=models.ManyToManyField(blank=True, to='people.City'),
        ),
        migrations.AlterField(
            model_name='query',
            name='query_country_tag',
            field=models.ManyToManyField(blank=True, to='people.Country'),
        ),
        migrations.AlterField(
            model_name='query',
            name='query_school_tag',
            field=models.ManyToManyField(blank=True, to='people.School'),
        ),
    ]
