from django import forms
from .models import ContactModel, ClientReview, Blog_Category, Blog_Details, Client_Logo, College_Model, Course_Model, Course_Collection, Sub_Collection, SubCollectionCategory, DetailsModel, ExamModel, ExamCategory, ExamDetails, EnquiryModel,  Enquiry_Model,EnquirySubmission,About_Video, FeaturedColleges, SliderImage
from django.core.exceptions import ValidationError
import re



class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'

class ClientReviewForm(forms.ModelForm):
    class Meta:
        model = ClientReview
        fields = '__all__'

class Blog_Category_Form(forms.ModelForm):
    class Meta:
        model = Blog_Category
        fields = '__all__'

class Blog_Details_Form(forms.ModelForm):
    class Meta:
        model = Blog_Details
        fields = '__all__'

class Client_Logo_Form(forms.ModelForm):
    class Meta:
        model = Client_Logo
        fields = '__all__'


class CollegeModelForm(forms.ModelForm):
    
    class Meta:
        model = College_Model
        fields = '__all__'


class FeaturedCollegesForm(forms.ModelForm):
    class Meta:
        model = FeaturedColleges
        fields = ['college_details']
        

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course_Model
        fields = '__all__'


class CourseCollectionForm(forms.ModelForm):
    class Meta:
        model = Course_Collection
        fields = '__all__'


# class Sub_Collection_Form(forms.ModelForm):
#     class Meta:
#         model = Sub_Collection
#         fields = '__all__'

class Sub_Collection_Form(forms.ModelForm):
    class Meta:
        model = Sub_Collection
        fields = ['course', 'course_type']


class SubCollectionCategoryForm(forms.ModelForm):
    class Meta:
         model = SubCollectionCategory
         fields = '__all__'


class DetailsModelForm(forms.ModelForm):
    class Meta:
         model = DetailsModel
         fields = '__all__'

class ExamForm(forms.ModelForm):
    class Meta:
         model = ExamModel
         fields = '__all__'


class ExamCategoryForm(forms.ModelForm):
    class Meta:
         model = ExamCategory
         fields = '__all__'

class ExamDetailsForm(forms.ModelForm):
    class Meta:
         model = ExamDetails
         fields = '__all__'

class EnquiryForm(forms.ModelForm):
    class Meta:
         model = EnquiryModel
         fields = '__all__'

class AboutVideoForm(forms.ModelForm):
    class Meta:
         model = About_Video
         fields = '__all__'

class SliderImageForm(forms.ModelForm):
    class Meta:
         model = SliderImage
         fields = '__all__'

# class Enquiry_Form(forms.ModelForm):
#     class Meta:
#          model = Enquiry_Model
#          fields = '__all__'


def validate_indian_phone_number(value):
    if not re.match(r'^[789]\d{9}$', value):
        raise ValidationError('Invalid Phone Number')

class Enquiry_Form(forms.ModelForm):
    phone = forms.CharField(validators=[validate_indian_phone_number])

    class Meta:
        model = Enquiry_Model
        fields = '__all__'


class OTPVerificationForm(forms.Form):
    otp = forms.CharField(max_length=6, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter OTP'}))

class EnquirySubmissionForm(forms.ModelForm):
    class Meta:
         model = EnquirySubmission
         fields = '__all__'