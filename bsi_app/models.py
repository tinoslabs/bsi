from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class ChatMessage(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
    

class ContactModel(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
class ClientReview(models.Model):
    client_name = models.CharField(max_length=100, null=True, blank=True)
    client_image = models.ImageField(upload_to='client_images/', null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    review_video = models.FileField(upload_to='review_videos/', null=True, blank=True)
    def __str__(self):
        return f"{self.client_name} - {self.designation}"
    

class Blog_Category(models.Model):
    category_name = models.CharField(max_length=100)
    blog_heading = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    main_image = models.ImageField(upload_to='images/')
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")

    def __str__(self):
        return self.category_name
    
class Blog_Details(models.Model):
    category = models.ForeignKey(Blog_Category,on_delete=models.CASCADE)
    blog_description = RichTextField(max_length=60000)
    blog_image = models.ImageField(upload_to='images/')
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")
    def __str__(self):
        return self.blog_description
    
class Client_Logo(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    logo = models.ImageField(upload_to='team_images/')

    def __str__(self):
        return self.name
    
