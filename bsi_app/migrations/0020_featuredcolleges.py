# Generated by Django 3.0.5 on 2024-08-11 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bsi_app', '0019_about_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedColleges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_in', to='bsi_app.College_Model')),
            ],
            options={
                'verbose_name': 'Featured College',
                'verbose_name_plural': 'Featured Colleges',
            },
        ),
    ]