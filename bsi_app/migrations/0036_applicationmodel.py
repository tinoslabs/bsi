# Generated by Django 3.2.10 on 2024-09-23 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bsi_app', '0035_delete_add_on_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('student_type', models.CharField(choices=[('full-time', 'Full-time'), ('part-time', 'Part-time'), ('online', 'Online'), ('on-campus', 'On-campus')], max_length=50)),
                ('degree', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True, null=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsi_app.collegemodel')),
            ],
        ),
    ]
