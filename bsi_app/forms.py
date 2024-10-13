from django import forms
from .models import  ClientReview, Blog_Category, Blog_Details, Client_Logo,  Course_Model,  ExamModel, ExamCategory, Enquiry_Submission, ExamDetails, About_Video, FeaturedColleges, SliderImage, headerMain,SubHeader,SubHeaderHeading,HeaderDetails,Notification,StateCategory,CollegeModel,AddOn_Course,ApplicationModel,EnquiryModel
from django.core.exceptions import ValidationError
import re


class Blog_Category_Form(forms.ModelForm):
    class Meta:
        model = Blog_Category
        fields = '__all__'

class Blog_Details_Form(forms.ModelForm):
    class Meta:
        model = Blog_Details
        fields = '__all__'


class ClientReviewForm(forms.ModelForm):
    class Meta:
        model = ClientReview
        fields = '__all__'

class EnquirySubmissionForm(forms.ModelForm):
    class Meta:
         model = Enquiry_Submission
         fields = '__all__'

class Client_Logo_Form(forms.ModelForm):
    class Meta:
        model = Client_Logo
        fields = '__all__'


class State_Form(forms.ModelForm):
    class Meta:
        model = StateCategory
        fields = '__all__'
        

class CollegeModelForm(forms.ModelForm):
    class Meta:
        model = CollegeModel
        fields = '__all__'


class FeaturedCollegesForm(forms.ModelForm):
    class Meta:
        model = FeaturedColleges
        fields = ['college_details','college_logo']
        

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course_Model
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




def validate_indian_phone_number(value):
    if not re.match(r'^[789]\d{9}$', value):
        raise ValidationError('Invalid Phone Number')




class OTPVerificationForm(forms.Form):
    otp = forms.CharField(max_length=6, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter OTP'}))


           
class headerMainForm(forms.ModelForm):
    class Meta:
        model = headerMain
        fields = ['main_heading']
       
from django.forms import formset_factory


class SubheaderForm(forms.ModelForm):
    class Meta:
        model = SubHeader
        fields = '__all__'

SubheaderFormSet = formset_factory(SubheaderForm, extra=1)  

class SubHeaderHeadingForm(forms.ModelForm):
    class Meta:
        model = SubHeaderHeading
        fields = '__all__'

SubheaderFormSet = formset_factory(SubheaderForm, extra=1)  


class SubHeaderHeadingForm(forms.ModelForm):
    class Meta:
        model = SubHeaderHeading
        fields = ['main_header', 'sub_header', 'sub_heading']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['main_header'].queryset = headerMain.objects.all()
        self.fields['sub_header'].queryset = SubHeader.objects.all()


class HeaderDetailsForm(forms.ModelForm):
    class Meta:
        model = HeaderDetails
        fields = '__all__'
        

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['message', 'read','notification_end_date','details']
        
class Add_On_Course_Form(forms.ModelForm):
    class Meta:
        model = AddOn_Course
        fields = '__all__'
    
    
from .models import NewsletterSubscription

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['college', 'email', 'phone']
        widgets = {
            'college': forms.Select(attrs={'id': 'college-select'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email id'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your mobile no'}),
        }
        

        
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = ApplicationModel
        fields = [
            'college',
            'first_name', 
            'last_name', 
            'email', 
            'phone', 
            'state', 
            'dob', 
            'student_type', 
            'degree',
            'message',
            'course'
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'student_type': forms.Select(choices=ApplicationModel.STUDENT_TYPE_CHOICES),
        }
    


    

