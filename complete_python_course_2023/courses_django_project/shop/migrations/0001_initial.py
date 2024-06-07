# Generated by Django 5.0.6 on 2024-06-05 03:35

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_ad', models.TimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('students_qty', models.IntegerField()),
                ('reviews_qty', models.IntegerField()),
                ('created_ad', models.TimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
    ]
