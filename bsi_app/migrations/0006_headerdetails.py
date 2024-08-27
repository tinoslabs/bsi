# Generated by Django 5.1 on 2024-08-23 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsi_app', '0005_subheaderheading'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(blank=True, null=True)),
                ('brochure', models.FileField(blank=True, null=True, upload_to='brochure/')),
                ('sub_heading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsi_app.subheaderheading')),
            ],
            options={
                'verbose_name': 'Header Details Model',
                'verbose_name_plural': 'Header Details Models',
            },
        ),
    ]