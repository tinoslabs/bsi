# Generated by Django 5.0.6 on 2024-10-13 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bsi_app', '0038_alter_enquiry_model_college_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactModel',
        ),
        migrations.RemoveField(
            model_name='subcollectioncategory',
            name='course',
        ),
        migrations.RemoveField(
            model_name='sub_collection',
            name='course',
        ),
        migrations.RemoveField(
            model_name='detailsmodel',
            name='sub_collection_category',
        ),
        migrations.RemoveField(
            model_name='enquiry_model',
            name='college',
        ),
        migrations.RemoveField(
            model_name='subcollectioncategory',
            name='sub_collection',
        ),
        migrations.RenameField(
            model_name='enquirymodel',
            old_name='Place',
            new_name='place',
        ),
        migrations.DeleteModel(
            name='Course_Collection',
        ),
        migrations.DeleteModel(
            name='DetailsModel',
        ),
        migrations.DeleteModel(
            name='Enquiry_Model',
        ),
        migrations.DeleteModel(
            name='Sub_Collection',
        ),
        migrations.DeleteModel(
            name='SubCollectionCategory',
        ),
    ]
