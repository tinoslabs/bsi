from rest_framework import serializers
from bsi_app.models import CollegeModel, StateCategory, ExamModel, ExamDetails, headerMain,SubHeader,SubHeaderHeading,HeaderDetails

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

    def create(self, validated_data):
        # Handle creation when category is nested (if it's not just an ID)
        category_data = validated_data.pop('category', None)

        if isinstance(category_data, dict):  # If the category data is nested, create it
            category = StateCategory.objects.create(**category_data)
        else:
            # If it's just an ID, get the StateCategory object
            category = category_data

        # Now create the CollegeModel instance and assign the category
        college_instance = CollegeModel.objects.create(category=category, **validated_data)

        return college_instance
    
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

    def create(self, validated_data):
        # Use the validated_data directly without separating the exam field
        return ExamDetails.objects.create(**validated_data)


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

    def create(self, validated_data):
        # main_header is a reference to the headerMain instance (primary key)
        main_header = validated_data.pop('main_header')

        # Create the SubHeader instance
        sub_header = SubHeader.objects.create(main_header=main_header, **validated_data)

        return sub_header
    
    
class SubHeaderHeadingSerializer(serializers.ModelSerializer):
    # Use PrimaryKeyRelatedField for relationships
    main_header = serializers.PrimaryKeyRelatedField(queryset=headerMain.objects.all())
    sub_header = serializers.PrimaryKeyRelatedField(queryset=SubHeader.objects.all())

    class Meta:
        model = SubHeaderHeading
        fields = ['id', 'main_header', 'sub_header', 'sub_heading']

    def create(self, validated_data):
        # Extract main_header and sub_header references
        main_header = validated_data.pop('main_header')
        sub_header = validated_data.pop('sub_header')

        # Create the SubHeaderHeading instance
        sub_header_heading = SubHeaderHeading.objects.create(
            main_header=main_header,
            sub_header=sub_header,
            **validated_data
        )
        return sub_header_heading
    
class HeaderDetailsSerializer(serializers.ModelSerializer):
    # Nested representation for SubHeaderHeading
    sub_heading = serializers.PrimaryKeyRelatedField(queryset=SubHeaderHeading.objects.all())

    class Meta:
        model = HeaderDetails
        fields = ['id', 'sub_heading', 'header_image', 'details', 'brochure']

    def create(self, validated_data):
        # Extract sub_heading instance
        sub_heading = validated_data.pop('sub_heading')

        # Create the HeaderDetails instance
        header_details = HeaderDetails.objects.create(sub_heading=sub_heading, **validated_data)

        return header_details