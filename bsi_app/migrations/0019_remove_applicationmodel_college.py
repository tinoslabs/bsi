# Generated by Django 5.1 on 2024-09-03 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bsi_app', '0018_alter_applicationmodel_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationmodel',
            name='college',
        ),
    ]