# Generated by Django 5.1 on 2024-08-23 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsi_app', '0002_sliderimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='headerMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_heading', models.CharField(max_length=100)),
            ],
        ),
    ]
