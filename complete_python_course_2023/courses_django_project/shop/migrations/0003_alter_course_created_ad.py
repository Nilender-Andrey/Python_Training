# Generated by Django 5.0.6 on 2024-06-11 04:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_course_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created_ad',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]