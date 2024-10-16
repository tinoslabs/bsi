# Generated by Django 5.0.7 on 2024-08-16 13:08

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_link', models.URLField(blank=True, null=True, unique=True)),
            ],
        ),
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
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client_Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('logo', models.ImageField(upload_to='team_images/')),
            ],
        ),
        migrations.CreateModel(
            name='ClientReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(blank=True, max_length=100, null=True)),
                ('client_image', models.ImageField(blank=True, null=True, upload_to='client_images/')),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('review_video', models.FileField(blank=True, null=True, upload_to='review_videos/')),
            ],
        ),
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
                ('college_description', models.TextField()),
                ('youtube_videos', models.URLField(blank=True, null=True, unique=True)),
                ('college_brochure', models.FileField(blank=True, null=True, upload_to='brochure/')),
                ('more_details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnquiryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Place', models.CharField(blank=True, max_length=20, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExamModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False, help_text='0-default,1-Hidden')),
            ],
        ),
        migrations.CreateModel(
            name='OTPVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('otp', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_description', ckeditor.fields.RichTextField(max_length=60000)),
                ('blog_image', models.ImageField(upload_to='images/')),
                ('status', models.BooleanField(default=False, help_text='0-default,1-Hidden')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsi_app.blog_category')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(blank=True, max_length=100, null=True)),
                ('course_type', models.CharField(choices=[('Professional', 'Professional Course'), ('Open', 'Open Course')], default='Professional', max_length=15)),
                ('course_description', models.TextField()),
                ('course_fees', models.CharField(blank=True, max_length=100, null=True)),
                ('course_duration', models.CharField(blank=True, max_length=100, null=True)),
                ('brochure', models.FileField(blank=True, null=True, upload_to='brochure/')),
                ('course_videos', models.URLField(blank=True, null=True, unique=True)),
                ('additional_details', models.TextField()),
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
        migrations.CreateModel(
            name='Enquiry_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Place', models.CharField(blank=True, max_length=20, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsi_app.college_model')),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry_Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsi_app.college_model')),
            ],
        ),
        migrations.CreateModel(
            name='ExamDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('videos', models.URLField(blank=True, null=True, unique=True)),
                ('exam_image', models.ImageField(blank=True, null=True, upload_to='exam_image/')),
                ('sample_papers', models.FileField(blank=True, null=True, upload_to='pdf/')),
                ('guide', models.FileField(blank=True, null=True, upload_to='pdf/')),
                ('brochure', models.FileField(blank=True, null=True, upload_to='brochure/')),
                ('more_details', models.TextField(blank=True, null=True)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsi_app.exammodel')),
            ],
            options={
                'verbose_name_plural': 'Exam Details',
            },
        ),
        migrations.CreateModel(
            name='ExamCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_type', models.CharField(choices=[('Overview', 'Overview'), ('Question Papers', 'Question Papers'), ('Date', 'Date'), ('Results', 'Results'), ('Cut Off', 'Cut Off'), ('Answer Key', 'Answer Key'), ('Analysis', 'Analysis'), ('Admit Card', 'Admit Card'), ('Center', 'Center'), ('Syllabus', 'Syllabus'), ('Mock Test', 'Mock Test')], default='Overview', max_length=50)),
                ('status', models.BooleanField(default=False, help_text='0-default,1-Hidden')),
                ('exam_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsi_app.exammodel')),
            ],
        ),
        migrations.CreateModel(
            name='FeaturedColleges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_in', to='bsi_app.college_model')),
            ],
            options={
                'verbose_name': 'Featured College',
                'verbose_name_plural': 'Featured Colleges',
            },
        ),
        migrations.CreateModel(
            name='Sub_Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_type', models.CharField(choices=[('Top Ranked Colleges', 'Top Ranked Colleges'), ('Popular Courses', 'Popular Courses'), ('Popular Specialization', 'Popular Specialization'), ('Colleges By Location', 'Colleges By Location'), ('Compare Colleges', 'Compare Colleges'), ('College Reviews', 'College Reviews'), ('Exams', 'Exams'), ('College Predictors', 'College Predictors'), ('Ask Current Students', 'Ask Current Students'), ('Rank Predictors', 'Rank Predictors'), ('Resources', 'Resources'), ('CAT Percentile Predictor', 'CAT Percentile Predictor')], default='Top Ranked Colleges', max_length=50)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsi_app.course_collection')),
            ],
            options={
                'verbose_name': 'Sub Collection',
                'verbose_name_plural': 'Sub Collections',
            },
        ),
        migrations.CreateModel(
            name='SubCollectionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(blank=True, max_length=100, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsi_app.course_collection')),
                ('sub_collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsi_app.sub_collection')),
            ],
            options={
                'verbose_name': 'Sub Collection Category',
                'verbose_name_plural': 'Sub Collection Categories',
            },
        ),
        migrations.CreateModel(
            name='DetailsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(blank=True, null=True)),
                ('videos', models.URLField(blank=True, null=True, unique=True)),
                ('more_details', models.TextField(blank=True, null=True)),
                ('sub_collection_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsi_app.subcollectioncategory')),
            ],
            options={
                'verbose_name': 'Details Model',
                'verbose_name_plural': 'Details Models',
            },
        ),
    ]
