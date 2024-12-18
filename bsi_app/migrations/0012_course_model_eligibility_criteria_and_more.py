# Generated by Django 5.1 on 2024-08-27 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsi_app', '0011_notification_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_model',
            name='eligibility_criteria',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='course_model',
            name='seat_availability',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course_model',
            name='additional_details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
