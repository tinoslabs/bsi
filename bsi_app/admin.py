from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Course_Collection)
admin.site.register(Sub_Collection)
admin.site.register(Course_Model)
admin.site.register(SubCollectionCategory)


@admin.register(EnquirySubmission)
class EnquirySubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'college', 'submitted_at')
    search_fields = ('name', 'email', 'phone', 'college__college_name')
    list_filter = ('submitted_at', 'college')

