# Generated by Django 5.0.7 on 2024-09-28 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsi_app', '0037_delete_application_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry_model',
            name='college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsi_app.collegemodel'),
        ),
        migrations.AlterField(
            model_name='enquiry_submission',
            name='college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsi_app.collegemodel'),
        ),
        migrations.DeleteModel(
            name='College_Model',
        ),
    ]