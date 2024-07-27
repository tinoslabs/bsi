from django import forms
from .models import ContactModel, ClientReview, Blog_Category, Blog_Details, Client_Logo, College_Model, Course_Model, Course_Collection, Sub_Collection, SubCollectionCategory, DetailsModel

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