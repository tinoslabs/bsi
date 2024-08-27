# Generated by Django 5.1 on 2024-08-27 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsi_app', '0013_alter_college_model_more_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_On_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(blank=True, max_length=100)),
                ('course_brochure', models.FileField(blank=True, upload_to='brochure/')),
                ('course_details', models.TextField(blank=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='add_on_courses', to='bsi_app.college_model')),
            ],
        ),
    ]
