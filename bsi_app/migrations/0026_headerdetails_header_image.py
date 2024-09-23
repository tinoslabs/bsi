# Generated by Django 3.2.10 on 2024-09-22 10:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bsi_app', '0025_college_model_header_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='headerdetails',
            name='header_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='header_image/'),
            preserve_default=False,
        ),
    ]
