# Generated by Django 2.2.4 on 2020-02-15 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200215_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='query_created_at',
            field=models.DateTimeField(),
        ),
    ]
