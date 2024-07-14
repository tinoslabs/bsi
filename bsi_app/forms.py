from django import forms
from .models import ContactModel, ClientReview, Blog_Category, Blog_Details, Client_Logo

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