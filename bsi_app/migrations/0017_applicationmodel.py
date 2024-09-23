# Generated by Django 5.1 on 2024-09-02 06:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsi_app', '0016_featuredcolleges_college_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('state', models.CharField(max_length=100)),
                ('pin_code', models.CharField(max_length=6)),
                ('dob', models.DateField()),
                ('student_type', models.CharField(choices=[('full-time', 'Full-time'), ('part-time', 'Part-time'), ('online', 'Online'), ('on-campus', 'On-campus')], max_length=200)),
                ('degree', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True, null=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsi_app.college_model')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsi_app.course_model')),
            ],
        ),
    ]