from rest_framework import serializers
from bsi_app.models import CollegeModel, StateCategory, ExamModel, ExamDetails, headerMain,SubHeader,SubHeaderHeading,HeaderDetails,Notification



class StateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StateCategory
        fields = ['id', 'state_name', 'state_image', 'status']


class CollegeModelSerializer(serializers.ModelSerializer):
    # Use PrimaryKeyRelatedField to link to StateCategory by its ID
    category = serializers.PrimaryKeyRelatedField(queryset=StateCategory.objects.all())

    total_fees_range = serializers.ReadOnlyField()

    class Meta:
        model = CollegeModel
        fields = [
            'id', 'category', 'college_name', 'header_image', 'place', 'logo', 'college_image',
            'total_course', 'rating', 'min_fee', 'max_fee', 'college_description', 'youtube_videos',
            'college_brochure', 'course_brochure', 'more_details', 'total_fees_range'
        ]

    
class ExamModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamModel
        fields = ['id', 'exam_name', 'status'] 
        
       
class ExamDetailsSerializer(serializers.ModelSerializer):
    exam = serializers.PrimaryKeyRelatedField(queryset=ExamModel.objects.all())
    
    class Meta:
        model = ExamDetails
        fields = [
            'id', 'exam', 'details', 'videos', 'exam_image', 
            'sample_papers', 'guide', 'brochure', 'more_details'
        ]


class HeaderMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = headerMain
        fields = ['id', 'main_heading']
        
        
class SubHeaderSerializer(serializers.ModelSerializer):
    # Use PrimaryKeyRelatedField for referencing headerMain
    main_header = serializers.PrimaryKeyRelatedField(queryset=headerMain.objects.all())

    class Meta:
        model = SubHeader
        fields = ['id', 'main_header', 'sub_header']

    
    
class SubHeaderHeadingSerializer(serializers.ModelSerializer):
    # Use PrimaryKeyRelatedField for relationships
    main_header = serializers.PrimaryKeyRelatedField(queryset=headerMain.objects.all())
    sub_header = serializers.PrimaryKeyRelatedField(queryset=SubHeader.objects.all())

    class Meta:
        model = SubHeaderHeading
        fields = ['id', 'main_header', 'sub_header', 'sub_heading']

    
class HeaderDetailsSerializer(serializers.ModelSerializer):
    # Nested representation for SubHeaderHeading
    sub_heading = serializers.PrimaryKeyRelatedField(queryset=SubHeaderHeading.objects.all())

    class Meta:
        model = HeaderDetails
        fields = ['id', 'sub_heading', 'header_image', 'details', 'brochure']


class NotificationSerializer(serializers.ModelSerializer):
    is_active = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'message', 'created_at', 'read', 'notification_end_date', 'details', 'is_active']

    def get_is_active(self, obj):
        return obj.is_active()