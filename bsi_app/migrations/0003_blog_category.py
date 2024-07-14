# Generated by Django 5.0.7 on 2024-07-14 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsi_app', '0002_clientreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('blog_heading', models.CharField(max_length=100)),
                ('date', models.DateField(blank=True, null=True)),
                ('main_image', models.ImageField(upload_to='images/')),
                ('status', models.BooleanField(default=False, help_text='0-default,1-Hidden')),
            ],
        ),
    ]
