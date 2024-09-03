from django.db import models
from ckeditor.fields import RichTextField

from django.utils import timezone


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
    
    
class College_Model(models.Model):
    college_name = models.CharField(max_length=200, null=True, blank=True)
    place = models.CharField(max_length=200, null=True, blank=True)
    logo = models.ImageField(upload_to='college_logos/')
    college_image = models.ImageField(upload_to='college_image/')
    total_course = models.PositiveIntegerField(null=True, blank=True)
    min_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    max_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    college_description  = models.TextField() 
    youtube_videos = models.URLField(max_length=200, unique=True, null=True, blank=True)
    college_brochure = models.FileField(upload_to='brochure/', null=True, blank=True)
    course_brochure = models.FileField(upload_to='brochure/', null=True, blank=True)
    more_details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.college_name

    @property
    def total_fees_range(self):
        if self.min_fee and self.max_fee:
            return f"₹{self.min_fee} L - ₹{self.max_fee} L"
        return None

class FeaturedColleges(models.Model):
    college_details = models.ForeignKey(College_Model, on_delete=models.CASCADE, related_name='featured_in')
    college_logo = models.ImageField(upload_to='college_logos/')
    def __str__(self):
        return f"{self.college_details.college_name} (Featured)"

    class Meta:
        verbose_name = "Featured College"
        verbose_name_plural = "Featured Colleges"
        
    

class Course_Model(models.Model):
    PROFESSIONAL_COURSE = 'Professional'
    OPEN_COURSE = 'Open'
    COURSE_TYPE_CHOICES = [
        (PROFESSIONAL_COURSE, 'Professional Course'),
        (OPEN_COURSE, 'Open Course'),
    ]
    
    college = models.ForeignKey(College_Model, on_delete=models.CASCADE, related_name='courses')
    course_name = models.CharField(max_length=100, null=True, blank=True)
    course_type = models.CharField(max_length=15, choices=COURSE_TYPE_CHOICES, default=PROFESSIONAL_COURSE)
    course_description = models.TextField()
    course_fees = models.CharField(max_length=100, null=True, blank=True)
    course_duration = models.CharField(max_length=100, null=True, blank=True)
    seat_availability = models.CharField(max_length=100, null=True, blank=True)
    eligibility_criteria = models.CharField(max_length=100, null=True, blank=True)
    brochure = models.FileField(upload_to='brochure/', null=True, blank=True)
    course_videos = models.URLField(max_length=200, unique=True, null=True, blank=True)
    additional_details = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.course_name or 'Unnamed Course'

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['course_name']


class Course_Collection(models.Model):
    courses = models.ManyToManyField(Course_Model, related_name='collections')

    def __str__(self):
        return ", ".join([course.course_name for course in self.courses.all()])

    class Meta:
        verbose_name = "Course Collection"
        verbose_name_plural = "Course Collections"


class Sub_Collection(models.Model):
    TOP_RANKED_COLLEGES = 'Top Ranked Colleges'
    POPULAR_COURSES = 'Popular Courses'
    POPULAR_SPECIALIZATION = 'Popular Specialization'
    COLLEGES_BY_LOCATION = 'Colleges By Location'
    COMPARE_COLLEGES = 'Compare Colleges'
    COLLEGE_REVIEWS = 'College Reviews'
    EXAMS = 'Exams'
    COLLEGE_PREDICTORS = 'College Predictors'
    ASK_CURRENT_STUDENTS = 'Ask Current Students'
    RANK_PREDICTORS = 'Rank Predictors'
    RESOURCES = 'Resources'
    CAT_PERCENTILE_PREDICTOR = 'CAT Percentile Predictor'
    
    COURSE_TYPE_CHOICES = [
        (TOP_RANKED_COLLEGES, 'Top Ranked Colleges'),
        (POPULAR_COURSES, 'Popular Courses'),
        (POPULAR_SPECIALIZATION, 'Popular Specialization'),
        (COLLEGES_BY_LOCATION, 'Colleges By Location'),
        (COMPARE_COLLEGES, 'Compare Colleges'),
        (COLLEGE_REVIEWS, 'College Reviews'),
        (EXAMS, 'Exams'),
        (COLLEGE_PREDICTORS, 'College Predictors'),
        (ASK_CURRENT_STUDENTS, 'Ask Current Students'),
        (RANK_PREDICTORS, 'Rank Predictors'),
        (RESOURCES, 'Resources'),
        (CAT_PERCENTILE_PREDICTOR, 'CAT Percentile Predictor'),
    ]

    course = models.ForeignKey(Course_Collection, on_delete=models.CASCADE)
    course_type = models.CharField(max_length=50, choices=COURSE_TYPE_CHOICES, default=TOP_RANKED_COLLEGES)

    def __str__(self):
        return f"{self.course} ({self.get_course_type_display()})"

    class Meta:
        verbose_name = "Sub Collection"
        verbose_name_plural = "Sub Collections"


class SubCollectionCategory(models.Model):
    course = models.ForeignKey(Course_Collection, on_delete=models.CASCADE)
    sub_collection = models.ForeignKey(Sub_Collection, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.sub_collection} - {self.sub_category}"

    class Meta:
        verbose_name = "Sub Collection Category" 
        verbose_name_plural = "Sub Collection Categories"


class DetailsModel(models.Model):
    sub_collection_category = models.ForeignKey(SubCollectionCategory, on_delete=models.CASCADE)
    details = models.TextField(null=True, blank=True)
    videos = models.URLField(max_length=200, unique=True, null=True, blank=True)
    more_details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.sub_collection_category.sub_category  # Assuming 'name' is a field in SubCollectionCategory

    class Meta:
        verbose_name = "Details Model"
        verbose_name_plural = "Details Models"


class ExamModel(models.Model):
    exam_name = models.CharField(max_length=200)
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")
    
    def __str__(self):
        return self.exam_name


class ExamDetails(models.Model):
    exam = models.ForeignKey(ExamModel, on_delete=models.CASCADE)
    details = models.TextField()
    videos = models.URLField(max_length=200, unique=True, null=True, blank=True)
    exam_image = models.ImageField(upload_to='exam_image/', null=True, blank=True)
    sample_papers = models.FileField(upload_to='pdf/', null=True, blank=True)
    guide = models.FileField(upload_to='pdf/', null=True, blank=True)
    brochure = models.FileField(upload_to='brochure/', null=True, blank=True)
    more_details = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.exam} Details"

    class Meta:
        verbose_name_plural = "Exam Details"


class ExamCategory(models.Model):
    OVERVIEW = 'Overview'
    QUESTION_PAPERS = 'Question Papers'
    DATE = 'Date'
    RESULTS = 'Results'
    CUT_OFF = 'Cut Off'
    ANSWER_KEY = 'Answer Key'
    ANALYSIS = 'Analysis'
    ADMIT_CARD = 'Admit Card'
    CENTER = 'Center'
    SYLLABUS = 'Syllabus'
    MOCK_TEST = 'Mock Test'
    
    EXAM_TYPE_CHOICES = [
        (OVERVIEW, 'Overview'),
        (QUESTION_PAPERS, 'Question Papers'),
        (DATE, 'Date'),
        (RESULTS, 'Results'),
        (CUT_OFF, 'Cut Off'),
        (ANSWER_KEY, 'Answer Key'),
        (ANALYSIS, 'Analysis'),
        (ADMIT_CARD, 'Admit Card'),
        (CENTER, 'Center'),
        (SYLLABUS, 'Syllabus'),
        (MOCK_TEST, 'Mock Test'),
    ]
    
    exam_name = models.ForeignKey('ExamModel', on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=50, choices=EXAM_TYPE_CHOICES, default=OVERVIEW)
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")
    
    def __str__(self):
        return f"{self.exam_name} - {self.exam_type}"
    

class EnquiryModel(models.Model):  
    name = models.CharField(max_length=100, blank=True, null=True)   
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    Place = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Enquiry_Model(models.Model):  
    college = models.ForeignKey(College_Model, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True, null=True)   
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    Place = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name
    
    
class About_Video(models.Model):
    video_link = models.URLField(max_length=200, unique=True, null=True, blank=True)

    
from django.utils import timezone
from datetime import timedelta

class OTPVerification(models.Model):
    phone = models.CharField(max_length=15)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return self.created_at >= timezone.now() - timedelta(minutes=5) 
    
class EnquirySubmission(models.Model):
    college = models.ForeignKey(College_Model, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15) 
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.college.college_name}"
    

class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider_images/')
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.caption if self.caption else "Slider Image"
    
    
    
class headerMain(models.Model):
    main_heading = models.CharField(max_length=100)
    
    def __str__(self):
        return self.main_heading 
     
class SubHeader(models.Model):
    main_header = models.ForeignKey(headerMain, on_delete=models.CASCADE)
    sub_header = models.CharField(max_length=100)
    
    def __str__(self):
        return self.sub_header 


    
class SubHeaderHeading(models.Model):
    main_header = models.ForeignKey(headerMain, on_delete=models.CASCADE)
    sub_header = models.ForeignKey(SubHeader, on_delete=models.CASCADE)
    sub_heading = models.CharField(max_length=100)
    
    def __str__(self):
        return self.sub_heading 
    
class HeaderDetails(models.Model):
    
    sub_heading = models.ForeignKey(SubHeaderHeading, on_delete=models.CASCADE)
    details = models.TextField(null=True, blank=True)
    brochure = models.FileField(upload_to='brochure/', null=True, blank=True)
    def __str__(self):
        return self.details
    
class Notification(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)    
    notification_end_date = models.DateTimeField()
    details = models.TextField(null=True, blank=True)
    def is_active(self):
        return self.notification_end_date >= timezone.now()
    
class Add_On_Course(models.Model):
    college = models.ForeignKey('College_Model', on_delete=models.CASCADE, related_name='add_on_courses')
    course_name = models.CharField(max_length=100, blank=True)
    course_brochure = models.FileField(upload_to='brochure/', blank=True)
    course_details = models.TextField(blank=True)

    def __str__(self):
        return self.course_name or "No Name Provided"
    
class NewsletterSubscription(models.Model):
    college = models.ForeignKey('College_Model', on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.email} - {self.college} - {self.phone}"
    
    
# class ApplicationModel(models.Model):
   
#     course = models.ForeignKey('Course_Model', on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.CharField(max_length=15)  # Adjusted max_length for flexibility
#     state = models.CharField(max_length=100)
#     pin_code = models.CharField(max_length=6)
#     dob = models.DateField()  # Using DateField

#     STUDENT_TYPE_CHOICES = [
#         ('full-time', 'Full-time'),
#         ('part-time', 'Part-time'),
#         ('online', 'Online'),
#         ('on-campus', 'On-campus'),
#     ]
    
#     student_type = models.CharField(max_length=50, choices=STUDENT_TYPE_CHOICES)
#     degree = models.CharField(max_length=100)
#     message = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name} - {self.course.course_name}"
    
    
class Application_Model(models.Model):
    college = models.ForeignKey('College_Model', on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)  # Adjusted max_length for flexibility
    state = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=6)
    dob = models.DateField()  # Using DateField

    STUDENT_TYPE_CHOICES = [
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('online', 'Online'),
        ('on-campus', 'On-campus'),
    ]
    
    student_type = models.CharField(max_length=50, choices=STUDENT_TYPE_CHOICES)
    degree = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.course}"
    
    
    


   


    




