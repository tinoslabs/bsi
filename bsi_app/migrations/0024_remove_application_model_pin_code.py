# Generated by Django 3.2.10 on 2024-09-22 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bsi_app', '0023_college_model_place_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application_model',
            name='pin_code',
        ),
    ]
