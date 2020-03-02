# Generated by Django 2.2.3 on 2020-03-01 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_follow'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('future', 'future'), ('student', 'student'), ('alumni', 'alumni')], max_length=20)),
                ('school', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('year_of_abroad_study', models.DateField()),
                ('job_before_abroad_study', models.CharField(max_length=100)),
                ('job_after_abroad_study', models.CharField(max_length=100)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
