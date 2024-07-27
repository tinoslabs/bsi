# Generated by Django 5.0.6 on 2024-07-24 08:42

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsi_app', '0005_client_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='College_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(blank=True, max_length=200, null=True)),
                ('place', models.CharField(blank=True, max_length=200, null=True)),
                ('logo', models.ImageField(upload_to='college_logos/')),
                ('college_image', models.ImageField(upload_to='college_image/')),
                ('total_course', models.PositiveIntegerField(blank=True, null=True)),
                ('min_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('max_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('college_description', models.CharField(blank=True, max_length=80000, null=True)),
                ('youtube_videos', models.URLField(blank=True, null=True, unique=True)),
                ('college_brochure', models.FileField(blank=True, null=True, upload_to='brochure/')),
                ('more_details', ckeditor.fields.RichTextField(blank=True, max_length=80000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(blank=True, max_length=100, null=True)),
                ('course_type', models.CharField(choices=[('Professional', 'Professional Course'), ('Open', 'Open Course')], default='Professional', max_length=15)),
                ('course_description', ckeditor.fields.RichTextField(blank=True, max_length=80000, null=True)),
                ('course_fees', models.CharField(blank=True, max_length=100, null=True)),
                ('course_duration', models.CharField(blank=True, max_length=100, null=True)),
                ('brochure', models.FileField(blank=True, null=True, upload_to='brochure/')),
                ('course_videos', models.URLField(blank=True, null=True, unique=True)),
                ('additional_details', ckeditor.fields.RichTextField(blank=True, max_length=80000, null=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='bsi_app.college_model')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
                'ordering': ['course_name'],
            },
        ),
        migrations.CreateModel(
            name='Course_Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.ManyToManyField(related_name='collections', to='bsi_app.course_model')),
            ],
            options={
                'verbose_name': 'Course Collection',
                'verbose_name_plural': 'Course Collections',
            },
        ),
    ]
