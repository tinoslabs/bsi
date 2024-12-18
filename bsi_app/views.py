from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import ChatMessage
from django.contrib.auth.decorators import login_required
from .models import  ClientReview,Blog_Category,Blog_Details,  Client_Logo, Course_Model, Course_Model, ExamModel, ExamCategory, ExamDetails, EnquiryModel, About_Video, FeaturedColleges, SliderImage, headerMain, SubHeader, SubHeaderHeading,HeaderDetails, Notification,NewsletterSubscription,CollegeModel,StateCategory,AddOn_Course,ApplicationModel,Enquiry_Submission
from .forms import  ClientReviewForm, Blog_Category_Form,Blog_Details_Form, Client_Logo_Form, CollegeModelForm,CourseForm,  ExamForm, ExamCategoryForm, ExamDetailsForm,EnquiryForm, AboutVideoForm, FeaturedCollegesForm, SliderImageForm,headerMainForm, SubheaderForm, SubHeaderHeadingForm, HeaderDetailsForm, HeaderDetailsForm, NotificationForm, Add_On_Course_Form,NewsletterForm,ApplicationForm,State_Form
from django.http import HttpResponseNotFound


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, ("Invalid username or password. Please try again...."))
            return redirect('user_login')
    return render(request, 'authenticate/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out.")
    return redirect('index')

@login_required(login_url='user_login')
def admin_dashboard(request):
    return render(request, 'admin_pages/admin_dashboard.html')

from django.db.models import Q

    
from django.urls import reverse

from django.db.models import OuterRef, Subquery, F

def index(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Our team will contact you soon.')
            return redirect('index')
    else:
        form = NewsletterForm()

    search_query = request.GET.get('query', '')
    if search_query:
        return redirect(f'{reverse("search_results")}?query={search_query}') 

    # Fetch all colleges ordered by their ID (or any date field)
   
    # colleges = CollegeModel.objects.filter(category__state_name__iexact='Kerala').order_by('-id')[:9]
    colleges = CollegeModel.objects.filter(category__state_name__iexact='Kerala')[:9]
    states = StateCategory.objects.all()
    # Use a set to keep track of displayed states
    
    blog_category = Blog_Category.objects.filter(status=0)
    courses = Course_Model.objects.all()
    exams = ExamModel.objects.all()
    add_on = AddOn_Course.objects.all()
    clients_review = ClientReview.objects.all()
    client_logo = Client_Logo.objects.all()
    notifications = Notification.objects.filter(notification_end_date__gte=timezone.now())
    main_header = headerMain.objects.all()
    sub_headers = SubHeader.objects.all()
    # sub_headings = SubHeaderHeading.objects.all().order_by('-id')
    sub_headings = SubHeaderHeading.objects.all()
    
    about = About_Video.objects.all()
    featured_colleges = FeaturedColleges.objects.all()
    slider_images = SliderImage.objects.all()
    footer_colleges = CollegeModel.objects.order_by('-id')[:5]
    footer_courses = Course_Model.objects.order_by('-id')[:7]
    footer_exams = ExamModel.objects.order_by('-id')[:7]

    context = {
        'colleges':colleges,
        'states':states,
        'blog_category':blog_category,
        'clients_review': clients_review,
        'client_logo': client_logo,
        'courses': courses,
        'notifications': notifications,
          # Pass the latest college instances
        
        'exam': exams,
        'add_on': add_on,
        'about': about,
        'featured_colleges': featured_colleges,
        'footer_colleges': footer_colleges,
        'footer_courses': footer_courses,
        'footer_exams': footer_exams,
        'slider_images': slider_images,
        'main_header': main_header,
        'sub_headers': sub_headers,
        'sub_headings': sub_headings,
        'unique_courses': Course_Model.objects.values('course_name').distinct(),
        'form': form
    }

    return render(request, 'index.html', context)


def search_results(request):
    search_query = request.GET.get('query', '')
    no_results = False

    colleges = CollegeModel.objects.none()
    courses = Course_Model.objects.none()
    exams = ExamModel.objects.none()
    add_on = AddOn_Course.objects.none()
    
    notifications = Notification.objects.filter(notification_end_date__gte=timezone.now())
    main_header = headerMain.objects.all()
    sub_headers = SubHeader.objects.all()
    sub_headings = SubHeaderHeading.objects.all()
    
    
    slider_images = SliderImage.objects.all()
    footer_colleges = CollegeModel.objects.order_by('-id')[:5]
    footer_courses = Course_Model.objects.order_by('-id')[:7]
    footer_exams = ExamModel.objects.order_by('-id')[:7]
    
    if search_query:
        colleges = CollegeModel.objects.filter(
            Q(college_name__icontains=search_query) | Q(place__icontains=search_query)
        )
        courses = Course_Model.objects.filter(
            Q(course_name__icontains=search_query)
        )
        exams = ExamModel.objects.filter(
            Q(exam_name__icontains=search_query)
        )
        add_on = AddOn_Course.objects.filter(
            Q(course_name__icontains=search_query)
        )
        
        # Check if there are any results
        if not colleges.exists() and not courses.exists() and not exams.exists() and not add_on.exists():
            no_results = True

    context = {
        'colleges': colleges,
        'courses': courses,
        'exams': exams,
        'add_on': add_on,
        'search_query': search_query,
        'no_results': no_results,
        'notifications': notifications,
        'main_header': main_header,
        'sub_headers': sub_headers,
        'sub_headings': sub_headings,
        
        'slider_images': slider_images,
        'footer_colleges': footer_colleges,
        'footer_courses': footer_courses,
        'footer_exams': footer_exams,
    }

    return render(request, 'search_results.html', context)

@login_required(login_url='user_login')
def add_blog_category(request):
    if request.method == 'POST':
        form = Blog_Category_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_blog_details') 
    else:
        form = Blog_Category_Form()

    return render(request, 'admin_pages/add_blog_category.html', {'form': form})

@login_required(login_url='user_login')
def view_blog_category(request):
    blog_category = Blog_Category.objects.all().order_by('-id')
    return render(request,'admin_pages/view_blog_category.html',{'blog_category':blog_category})

@login_required(login_url='user_login')
def update_blog_category(request,id):
    blog_category = get_object_or_404(Blog_Category, id=id)
    if request.method == 'POST':
        form = Blog_Category_Form(request.POST, request.FILES, instance=blog_category)
        if form.is_valid():
            form.save()
            return redirect('view_blog_category')
    else:
        form = Blog_Category_Form(instance=blog_category)
    return render(request, 'admin_pages/update_blog_category.html', {'form': form, 'blog_category': blog_category})


@login_required(login_url='user_login')
def delete_blog_category(request,id):
    blog_category = Blog_Category.objects.get(id=id)
    blog_category.delete()
    return redirect('view_blog_category')

@login_required(login_url='user_login')
def add_blog_details(request):
    categories = Blog_Category.objects.all() 
    if request.method == 'POST':
        blog_details = Blog_Details_Form(request.POST, request.FILES)
        if blog_details.is_valid():
            blog_details.save()
            return redirect('view_blog_details')  
    else:
        blog_details = Blog_Details_Form()

    return render(request, 'admin_pages/add_blog_details.html', {'blog_details': blog_details,'categories':categories})


@login_required(login_url='user_login')
def view_blog_details(request):
    blog_details = Blog_Details.objects.all().order_by('-id')
    return render(request,'admin_pages/view_blog_details.html',{'blog_details':blog_details})

@login_required(login_url='user_login')
def update_blog_details(request, id):
    blog_details = get_object_or_404(Blog_Details, id=id)
    if request.method == 'POST':
        form = Blog_Details_Form(request.POST, request.FILES, instance=blog_details)
        if form.is_valid():
            form.save()
            return redirect('view_blog_details')
    else:
        form = Blog_Details_Form(instance=blog_details)
        categories = Blog_Category.objects.all()
    return render(request, 'admin_pages/update_blog_details.html', {'form': form, 'blog_details': blog_details,'categories':categories})


@login_required(login_url='user_login')
def delete_blog_details(request,id):
    blog_details = Blog_Details.objects.get(id=id)
    blog_details.delete()
    return redirect('view_blog_details')


@login_required(login_url='user_login')
def News_Letter_view(request):
    data = NewsletterSubscription.objects.all()
    return render(request, 'admin_pages/News_Letter_view.html',{'data':data})

@login_required(login_url='user_login')
def delete_news_letter(request,id):
    contact = NewsletterSubscription.objects.get(id=id)
    contact.delete()
    return redirect('News_Letter_view')

from django.http import JsonResponse
from .models import ChatMessage

@login_required(login_url='user_login')
def chatbot_message_view(request):
    chatbot = ChatMessage.objects.all().order_by('-id')
    return render(request,'admin_pages/chatbot_message_view.html',{'chatbot':chatbot})

@login_required(login_url='user_login')
def delete_message(request,id):
    chatbot = ChatMessage.objects.get(id=id)
    chatbot.delete()
    return redirect('chatbot_message_view')


@login_required(login_url='user_login')
def contact_view(request):
    contacts = EnquiryModel.objects.all().order_by('-id')
    return render(request, 'admin_pages/contact_view.html', {'contacts': contacts})


@login_required(login_url='user_login')
def delete_contact(request,id):
    contact = EnquiryModel.objects.get(id=id)
    contact.delete()
    return redirect('contact_view')


@login_required(login_url='user_login')
def enquiry_view(request):
    enquiry = EnquiryModel.objects.all().order_by('-id')
    return render(request,'admin_pages/enquiry_view.html',{'enquiry':enquiry})


@login_required(login_url='user_login')
def demo(request):
    enquiry = EnquiryModel.objects.all().order_by('-id')
    return render(request,'admin_pages/demo.html',{'enquiry':enquiry})


@login_required(login_url='user_login')
def delete_enquiry(request,id):
    enquiry = EnquiryModel.objects.get(id=id)
    enquiry.delete()
    return redirect('enquiry_view')


@login_required(login_url='user_login')
def add_client_reviews(request):
    if request.method == 'POST':
        form = ClientReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_client_reviews') 
    else:
        form = ClientReviewForm()

    return render(request, 'admin_pages/add_client_reviews.html', {'form': form})


@login_required(login_url='user_login')
def view_client_reviews(request):
    client_reviews = ClientReview.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_client_reviews.html', {'client_reviews': client_reviews})


@login_required(login_url='user_login')
def update_client_reviews(request, id):
    client_reviews = get_object_or_404(ClientReview, id=id)
    if request.method == 'POST':
        form = ClientReviewForm(request.POST, request.FILES, instance=client_reviews)
        if form.is_valid():
            form.save()
            return redirect('view_client_reviews')
    else:
        form = ClientReviewForm(instance=client_reviews)
    return render(request, 'admin_pages/update_client_reviews.html', {'form': form, 'client_reviews': client_reviews})

    
@login_required(login_url='user_login')
def delete_client_review(request,id):
    client_reviews = ClientReview.objects.get(id=id)
    client_reviews.delete()
    return redirect('view_client_reviews')


@login_required(login_url='user_login')
def create_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create_exam_details') 
    else:
        form = ExamForm()

    return render(request, 'admin_pages/create_exam.html', {'form': form})


@login_required(login_url='user_login')
def view_exam(request):
    exams = ExamModel.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_exam.html', {'exams': exams})


@login_required(login_url='user_login')
def update_exam(request, id):
    exams = get_object_or_404(ExamModel, id=id)
    if request.method == 'POST':
        form = ExamForm(request.POST, request.FILES, instance=exams)
        if form.is_valid():
            form.save()
            return redirect('view_exam')
    else:
        form = ExamForm(instance=exams)
    return render(request, 'admin_pages/update_exam.html', {'form': form, 'exams': exams})


@login_required(login_url='user_login')
def delete_exam(request,id):
    exams = ExamModel.objects.get(id=id)
    exams.delete()
    return redirect('view_exam')


@login_required(login_url='user_login')
def create_exam_category(request):
    if request.method == 'POST':
        form = ExamCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_exam_category') 
    else:
        form = ExamCategoryForm()

    return render(request, 'admin_pages/create_exam_category.html', {'form': form})


@login_required(login_url='user_login')
def view_exam_category(request):
    category = ExamCategory.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_exam_category.html', {'category': category})


@login_required(login_url='user_login')
def update_exam_category(request, pk):
    exam_category = get_object_or_404(ExamCategory, pk=pk)
    if request.method == 'POST':
        form = ExamCategoryForm(request.POST, request.FILES, instance=exam_category)
        if form.is_valid():
            form.save()
            return redirect('view_exam_category')  # Replace with your view name
    else:
        form = ExamCategoryForm(instance=exam_category)
    
    return render(request, 'admin_pages/update_exam_category.html', {'form': form})


@login_required(login_url='user_login')
def delete_exam_category(request, pk):
    exam_category = get_object_or_404(ExamCategory, pk=pk)
    exam_category.delete()
    return redirect('some_view_name')  # Replace with your view name
    
    
@login_required(login_url='user_login')
def create_exam_details(request):
    if request.method == 'POST':
        form = ExamDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_exam_details') 
    else:
        form = ExamDetailsForm()

    return render(request, 'admin_pages/create_exam_details.html', {'form': form})


@login_required(login_url='user_login')
def view_exam_details(request):
    category = ExamDetails.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_exam_details.html', {'category': category})


@login_required(login_url='user_login')
def update_exam_details(request, id):
    exam_detail = get_object_or_404(ExamDetails, id=id)
    if request.method == 'POST':
        form = ExamDetailsForm(request.POST, request.FILES, instance=exam_detail)
        if form.is_valid():
            form.save()
            return redirect('view_exam_details')
    else:
        form = ExamDetailsForm(instance=exam_detail)

    exams = ExamModel.objects.all()
    # Use 'exam_name' to filter categories
    categories = ExamCategory.objects.filter(exam_name=exam_detail.exam)  
    context = {
        'form': form,
        'exams': exams,
        'categories': categories,
        'exam_detail': exam_detail,
    }
    return render(request, 'admin_pages/update_exam_details.html', context)


@login_required(login_url='user_login')
def delete_exam_details(request,id):
    exam_detail = ExamDetails.objects.get(id=id)
    exam_detail.delete()
    return redirect('view_exam_details')


@login_required(login_url='user_login')
def add_clients_logo(request):
    if request.method == 'POST':
        form = Client_Logo_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_clients_logo') 
    else:
        form = Client_Logo_Form()

    return render(request, 'admin_pages/add_clients_logo.html', {'form': form})

@login_required(login_url='user_login')
def view_clients_logo(request):
    logo = Client_Logo.objects.all().order_by('-id')
    return render(request,'admin_pages/view_clients_logo.html',{'logo':logo})

@login_required(login_url='user_login')
def update_clients_logo(request,id):
    logos = get_object_or_404(Client_Logo, id=id)
    if request.method == 'POST':
        form = Client_Logo_Form(request.POST, request.FILES, instance=logos)
        if form.is_valid():
            form.save()
            return redirect('view_clients_logo')
    else:
        form = Client_Logo_Form(instance=logos)
    return render(request, 'admin_pages/update_clients_logo.html', {'form': form, 'logos': logos})

@login_required(login_url='user_login')
def delete_clients_logo(request,id):
    logos = Client_Logo.objects.get(id=id)
    logos.delete()
    return redirect('view_clients_logo')

# ///// College Section Start //////

@login_required(login_url='user_login')
def add_state_category(request):
    if request.method == 'POST':
        form = State_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create_college') 
    else:
        form = State_Form()

    return render(request, 'admin_pages/add_state_category.html', {'form': form})

@login_required(login_url='user_login')
def view_state_category(request):
    state_category = StateCategory.objects.all().order_by('-id')
    return render(request,'admin_pages/view_state_category.html',{'state_category':state_category})

@login_required(login_url='user_login')
def update_state_category(request,id):
    category = get_object_or_404(StateCategory, id=id)
    if request.method == 'POST':
        form = State_Form(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('view_state_category')
    else:
        form = State_Form(instance=category)
    return render(request, 'admin_pages/update_state_category.html', {'form': form, 'category': category})


@login_required(login_url='user_login')
def delete_state_category(request,id):
    category = StateCategory.objects.get(id=id)
    category.delete()
    return redirect('view_state_category')

@login_required(login_url='user_login')
def create_college(request):
    categories = StateCategory.objects.all()
    if request.method == 'POST':
        form = CollegeModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_college')  # Replace with your success URL
    else:
        form = CollegeModelForm()
    return render(request, 'admin_pages/create_college.html', {'form': form,'categories':categories})

@login_required(login_url='user_login')
def view_college(request):
    colleges = CollegeModel.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_college.html', {'colleges': colleges})


@login_required(login_url='user_login')
def update_college(request, college_id):
    college = get_object_or_404(CollegeModel, id=college_id)
    categories = StateCategory.objects.all()
    if request.method == 'POST':
        form = CollegeModelForm(request.POST, request.FILES, instance=college)
        if form.is_valid():
            form.save()
            return redirect('view_college')  # Replace with your view college URL
    else:
        form = CollegeModelForm(instance=college)
    
    return render(request, 'admin_pages/update_college.html', {'form': form, 'college': college,'categories':categories})


@login_required(login_url='user_login')
def delete_college(request, college_id):
    college = get_object_or_404(CollegeModel, id=college_id)
    college.delete()
    return redirect('view_college')  # Replace 'view_colleges' with your view name for viewing all colleges

# ///// Course Section Start //////
@login_required(login_url='user_login')
def create_course(request):
    college = CollegeModel.objects.all()
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_course')  # Replace 'view_courses' with your view name for viewing all courses
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = CourseForm()
    return render(request, 'admin_pages/create_course.html', {'form': form, 'college': college})


@login_required(login_url='user_login')
def view_course(request):
    courses = Course_Model.objects.select_related('college').all()
    return render(request, 'admin_pages/view_course.html', {'courses': courses})

@login_required(login_url='user_login')
def update_course(request, course_id):
    course = get_object_or_404(Course_Model, id=course_id)
    college = CollegeModel.objects.all() 
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('view_course')  # Redirect to the view courses page
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = CourseForm(instance=course)
    
    return render(request, 'admin_pages/update_course.html', {'form': form, 'college': college, 'course': course})


@login_required(login_url='user_login')
def delete_course(request, id):
    course = get_object_or_404(Course_Model, id=id)
    course.delete()
    return redirect('view_course')

@login_required(login_url='user_login')
def create_add_on_course(request):
    college = CollegeModel.objects.all()
    if request.method == 'POST':
        form = Add_On_Course_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_add_on_course')  
        else:
            print(form.errors)  
    else:
        form = Add_On_Course_Form()
    return render(request, 'admin_pages/create_add_on_course.html', {'form': form, 'college': college})

@login_required(login_url='user_login')
def view_add_on_course(request):
    courses = AddOn_Course.objects.select_related('college').all()
    return render(request, 'admin_pages/view_add_on_course.html', {'courses': courses})

@login_required(login_url='user_login')
def update_add_on_course(request, id):
    course = get_object_or_404(AddOn_Course, id=id)
    college = CollegeModel.objects.all() 
    if request.method == 'POST':
        form = Add_On_Course_Form(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('view_add_on_course')  # Redirect to the view courses page
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = Add_On_Course_Form(instance=course)
    
    return render(request, 'admin_pages/update_add_on_course.html', {'form': form, 'college': college, 'course': course})


@login_required(login_url='user_login')
def delete_add_on_course(request, id):
    course = get_object_or_404(AddOn_Course, id=id)
    course.delete()
    return redirect('view_add_on_course')


def create_featured_colleges(request):
    if request.method == 'POST':
        print(request.FILES)  # Debug: Check what files are being uploaded
        form = FeaturedCollegesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_featured_colleges')
        else:
            print(form.errors)  # Debug: Print form errors if any
    else:
        form = FeaturedCollegesForm()
    return render(request, 'admin_pages/create_featured_colleges.html', {'form': form})


@login_required(login_url='user_login')
def view_featured_colleges(request):
    featured_colleges = FeaturedColleges.objects.all()
    return render(request, 'admin_pages/view_featured_colleges.html', {'featured_colleges': featured_colleges})

def update_featured_colleges(request, pk):
    college = get_object_or_404(FeaturedColleges, pk=pk)
    if request.method == 'POST':
        form = FeaturedCollegesForm(request.POST, request.FILES, instance=college)
        if form.is_valid():
            form.save()
            return redirect('view_featured_colleges')  # Redirect to the view after saving
    else:
        form = FeaturedCollegesForm(instance=college)
    return render(request, 'admin_pages/update_featured_colleges.html', {'form': form})


def delete_featured_colleges(request, pk):
    college = get_object_or_404(FeaturedColleges, pk=pk)
    
    college.delete()
    return redirect('view_featured_colleges')  # Redirect to the view after deletion

@login_required(login_url='user_login')
def create_header_main(request):
    if request.method == 'POST':
        form = headerMainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_sub_header')  
    else:
        form = headerMainForm()
    return render(request, 'admin_pages/create_header_main.html', {'form': form})
 

@login_required(login_url='user_login')
def view_header_main(request):
    main_heading = headerMain.objects.all()
    return render(request, 'admin_pages/view_header_main.html', {'main_heading': main_heading})

@login_required(login_url='user_login')
def update_header_main(request, pk):
    main_heading = get_object_or_404(headerMain, pk=pk)
    if request.method == 'POST':
        form = headerMainForm(request.POST, instance=main_heading)
        if form.is_valid():
            form.save()
            return redirect('view_header_main')  # Redirect to the view after saving
    else:
        form = headerMainForm(instance=main_heading)
    return render(request, 'admin_pages/update_header_main.html', {'form': form})

def delete_header_main(request, pk):
    main_heading = get_object_or_404(headerMain, pk=pk)
    main_heading.delete()
    return redirect('view_header_main')

from .forms import SubheaderFormSet

@login_required(login_url='user_login')
def create_sub_header(request):
    if request.method == 'POST':
        form = SubheaderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_sub_header_heading') 
    else:
        form = SubheaderForm()
      
    main_headers = headerMain.objects.all()
    return render(request, 'admin_pages/create_sub_header.html', {'form': form, 'main_headers': main_headers})


@login_required(login_url='user_login')
def update_sub_header(request, pk):
    subheader = get_object_or_404(SubHeader, pk=pk)
    
    if request.method == 'POST':
        form = SubheaderForm(request.POST, instance=subheader)
        if form.is_valid():
            form.save()
            return redirect('view_sub_header')  # Redirect to a view that lists subheaders
    else:
        form = SubheaderForm(instance=subheader)
    
    main_headers = headerMain.objects.all()
    return render(request, 'admin_pages/update_sub_header.html', {'form': form, 'main_headers': main_headers})


@login_required(login_url='user_login')
def delete_sub_header(request, pk):
    subheader = get_object_or_404(SubHeader, pk=pk) 
    subheader.delete()
    return redirect('view_sub_header')  # Redirect to a view that lists subheaders



@login_required(login_url='user_login')
def create_sub_header_heading(request):
    if request.method == 'POST':
        form = SubHeaderHeadingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_header_details')  
    else:
        form = SubHeaderHeadingForm()

    main_headers = headerMain.objects.all()

    return render(request, 'admin_pages/create_sub_header_heading.html', {
        'form': form,
        'main_headers': main_headers,
    })

@login_required(login_url='user_login')
def get_sub_headers(request):
    main_header_id = request.GET.get('main_header_id')
    sub_headers = SubHeader.objects.filter(main_header_id=main_header_id)
    options = '<option value="">Select Sub Header</option>'
    for sub_header in sub_headers:
        options += f'<option value="{sub_header.id}">{sub_header.sub_header}</option>'
    return HttpResponse(options)

@login_required(login_url='user_login')
def get_subheaders(request, main_header_id):
    sub_headers = SubHeader.objects.filter(main_header_id=main_header_id)
    data = {
        'sub_headers': list(sub_headers.values('id', 'sub_header'))
    }
    return JsonResponse(data)

@login_required(login_url='user_login')
def update_sub_header_heading(request, pk):
    sub_header_heading = SubHeaderHeading.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = SubHeaderHeadingForm(request.POST, instance=sub_header_heading)
        if form.is_valid():
            form.save()
            return redirect('view_sub_header_heading')
    else:
        form = SubHeaderHeadingForm(instance=sub_header_heading)

    main_headers = headerMain.objects.all()
    sub_headers = SubHeader.objects.filter(main_header=sub_header_heading.main_header)

    return render(request, 'admin_pages/update_sub_header_heading.html', {
        'form': form,
        'main_headers': main_headers,
        'sub_headers': sub_headers,
        'selected_main_header': sub_header_heading.main_header,
        'selected_sub_header': sub_header_heading.sub_header,
    })


@login_required(login_url='user_login')
def delete_sub_header_heading(request, pk):
    sub_header_heading = get_object_or_404(SubHeaderHeading, pk=pk)
    sub_header_heading.delete()
    return redirect('view_sub_header_heading')


@login_required(login_url='user_login')
def view_sub_header_heading(request):
    sub_header_headings = SubHeaderHeading.objects.all()
    return render(request, 'admin_pages/view_sub_header_heading.html', {'sub_header_headings': sub_header_headings})

@login_required(login_url='user_login')
def view_sub_header(request):
    sub_heading = SubHeader.objects.all()
    return render(request, 'admin_pages/view_sub_header.html', {'sub_heading': sub_heading})



@login_required(login_url='user_login')
def add_header_details(request):
    # Query all SubHeaderHeading objects
    sub_headings = SubHeaderHeading.objects.all()
    
    # Prepare a list of formatted sub_headings
    formatted_sub_headings = []
    for sh in sub_headings:
        main_header = sh.main_header.main_heading
        sub_header = sh.sub_header.sub_header
        sub_heading = sh.sub_heading
        formatted_sub_headings.append({
            'id': sh.id,
            'text': f"({main_header}) - ({sub_header}) - {sub_heading}"
        })
    
    if request.method == 'POST':
        form = HeaderDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_header_details')
    else:
        form = HeaderDetailsForm()

    return render(request, 'admin_pages/add_header_details.html', {
        'form': form,
        'sub_headings': formatted_sub_headings
    })




@login_required(login_url='user_login')
def view_header_details(request):
    header_details = HeaderDetails.objects.all()
    return render(request, 'admin_pages/view_header_details.html', {'header_details': header_details})

@login_required(login_url='user_login')
def update_header_details(request, pk):
    header_detail = get_object_or_404(HeaderDetails, pk=pk)
    
    if request.method == 'POST':
        form = HeaderDetailsForm(request.POST, request.FILES, instance=header_detail)
        if form.is_valid():
            form.save()
            return redirect('view_header_details')
    else:
        form = HeaderDetailsForm(instance=header_detail)
    
    # Prepare a list of formatted sub_headings
    sub_headings = SubHeaderHeading.objects.all()
    formatted_sub_headings = []
    for sh in sub_headings:
        main_header = sh.main_header.main_heading
        sub_header = sh.sub_header.sub_header
        sub_heading = sh.sub_heading
        formatted_sub_headings.append({
            'id': sh.id,
            'text': f"({main_header}) - ({sub_header}) - {sub_heading}"
        })
    
    return render(request, 'admin_pages/update_header_details.html', {
        'form': form,
        'sub_headings': formatted_sub_headings,
        'header_detail': header_detail
    })

@login_required(login_url='user_login')
def delete_header_details(request, pk):
    detail = get_object_or_404(HeaderDetails, pk=pk)
    detail.delete()
    return redirect('view_header_details')
    

@login_required(login_url='user_login')
def create_slider(request):
    if request.method == 'POST':
        form = SliderImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_slider')
    else:
        form = SliderImageForm()

    slider_images = SliderImage.objects.all()
    return render(request, 'admin_pages/create_slider.html', {'form': form, 'slider_images': slider_images})


@login_required(login_url='user_login')
def update_slider(request, pk):
    slider_image = get_object_or_404(SliderImage, pk=pk)
    if request.method == 'POST':
        form = SliderImageForm(request.POST, request.FILES, instance=slider_image)
        if form.is_valid():
            form.save()
            return redirect('view_slider')  # Redirect to the view page after updating
    else:
        form = SliderImageForm(instance=slider_image)
    return render(request, 'admin_pages/update_slider.html', {'form': form, 'slider_image': slider_image})


@login_required(login_url='user_login')
def delete_slider(request, pk):
    slider_image = get_object_or_404(SliderImage, pk=pk)
    slider_image.delete()
    return redirect('view_slider')

@login_required(login_url='user_login')
def view_slider(request):
    slider = SliderImage.objects.all()
    return render(request, 'admin_pages/view_slider.html', {'slider': slider})





def load_courses(request):
    college_id = request.GET.get('college')
    courses = Course_Model.objects.filter(college_id=college_id).all()
    return JsonResponse(list(courses.values('id', 'course_name')), safe=False)


def submit_query(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and phone_number and email and message:
            # Save the data to the ChatMessage model
            ChatMessage.objects.create(
                name=name,
                phone_number=phone_number,
                email=email,
                message=message
            )
            return JsonResponse({'message': 'Data saved successfully'}, status=200)
        else:
            return JsonResponse({'error': 'All fields are required'}, status=400)

def service(request):
    return render(request,'service.html')

def exam(request):
    return render(request,'exam.html')

def blog(request):
    blog_category = Blog_Category.objects.filter(status=0)
    return render(request,'blog.html',{'blog_category':blog_category})

def blog_details(request, blog_heading):
    exam = ExamModel.objects.all()
    courses = Course_Model.objects.all()

    blog = Blog_Category.objects.all()
    main_header = headerMain.objects.all()
    sub_headers = SubHeader.objects.all()
    sub_headings = SubHeaderHeading.objects.all()
    footer_colleges = CollegeModel.objects.order_by('-id')[:5]
    footer_courses = Course_Model.objects.order_by('-id')[:7]
    footer_exams = ExamModel.objects.order_by('-id')[:7]
    notifications = Notification.objects.filter(notification_end_date__gte=timezone.now())
    
    category = get_object_or_404(Blog_Category, blog_heading=blog_heading, status=False)
    if category:
        blog_details = Blog_Details.objects.filter(category=category, status=False)
        context = {'blog_details': blog_details, 'category_name': category,'blog':blog,'courses':courses,'exam':exam,'footer_colleges':footer_colleges,'footer_courses':footer_courses,'footer_exams':footer_exams,'main_header':main_header,'sub_headers':sub_headers,'sub_headings':sub_headings,'notifications':notifications}
        return render(request, "blog-details.html", context)
    else:
        messages.warning(request, "No such category found")
        return render(request, 'blog-details.html')



def college_details(request, college_name):
    college = get_object_or_404(CollegeModel, college_name=college_name)
    
    if request.method == 'POST':
        # Determine which form was submitted
        if 'first_name' in request.POST:  # Assuming 'first_name' is unique to ApplicationForm
            application_form = ApplicationForm(request.POST)
            if application_form.is_valid():
                application_form.save()
                messages.success(request, 'Your application has been submitted successfully.')
                return redirect('college_details', college_name=college_name)
        else:
            form = EnquiryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Our team will contact you soon.')
                return redirect('college_details', college_name=college_name)
    else:
        form = EnquiryForm()
        application_form = ApplicationForm()

    # other context data
    exam = ExamModel.objects.all()
    colleges = CollegeModel.objects.all()
    course = Course_Model.objects.all()
    # courses = college.courses.all()
   
    clients_review = ClientReview.objects.all()

    main_header = headerMain.objects.all()
    sub_headers = SubHeader.objects.all()
    notifications = Notification.objects.filter(notification_end_date__gte=timezone.now())
    sub_headings = SubHeaderHeading.objects.all()
    footer_colleges = CollegeModel.objects.order_by('-id')[:5]
    footer_courses = Course_Model.objects.order_by('-id')[:7]
    footer_exams = ExamModel.objects.order_by('-id')[:7]
    
    return render(request, 'college_details.html', {
        'form': form,
        'application_form': application_form,
        'college': college,
        # 'courses': courses,
        'colleges': colleges,

        'clients_review':clients_review,

        'exam' : exam,
        'course' : course,
        'footer_colleges':footer_colleges,
        'footer_courses':footer_courses,
        'footer_exams':footer_exams,
        'main_header':main_header,
        'sub_headers':sub_headers,
        'sub_headings':sub_headings,
        'notifications':notifications,
    })


def download_brochure(request):
    if request.method == 'POST':
        college_id = request.POST.get('college_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        try:
            college = CollegeModel.objects.get(id=college_id)
            Enquiry_Submission.objects.create(
                college=college,
                name=name,
                email=email,
                phone=phone
            )
            brochure_url = college.college_brochure.url
            return JsonResponse({'success': True, 'brochure_url': brochure_url})
        except CollegeModel.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'College not found'})

    return JsonResponse({'success': False, 'message': 'Invalid request'})

@login_required(login_url='user_login')
def Application_view(request):
    data = ApplicationModel.objects.all()
    return render(request,'admin_pages/Application_view.html',{'data':data})

@login_required(login_url='user_login')
def delete_application(request, pk):
    data = get_object_or_404(ApplicationModel, id=pk)
    data.delete()
    return redirect('Application_view') 

@login_required(login_url='user_login')
def enquiry_submition_view(request):
    data = Enquiry_Submission.objects.all()
    return render(request,'admin_pages/enquiry_submition_view.html',{'data':data})

@login_required(login_url='user_login')
def delete_enquiry_submition(request, pk):
    data = get_object_or_404(Enquiry_Submission, id=pk)
    data.delete()
    return redirect('enquiry_submition_view') 

@login_required(login_url='user_login')
def create_about_video(request):
    if request.method == 'POST':
        form = AboutVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_about_video') 
    else:
        form = AboutVideoForm()

    return render(request, 'admin_pages/create_about_video.html', {'form': form})
    
@login_required(login_url='user_login')
def view_about_video(request):
    links = About_Video.objects.all()
    return render(request,'admin_pages/view_about_video.html',{'links':links})
    
@login_required(login_url='user_login')
def update_about_video(request, id):
    video = get_object_or_404(About_Video, id=id)

    if request.method == 'POST':
        form = AboutVideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect('view_about_video')
    else:
        form = AboutVideoForm(instance=video)

    return render(request, 'admin_pages/update_about_video.html', {'form': form})

@login_required(login_url='user_login')
def delete_about_video(request, id):
    video = get_object_or_404(About_Video, id=id)
    video.delete()
    return redirect('view_about_video')


def course_details(request, id):
    course = get_object_or_404(Course_Model, id=id)
    
    if request.method == 'POST':
        if 'first_name' in request.POST:  # Assuming 'first_name' is unique to ApplicationForm
            application_form = ApplicationForm(request.POST)
            if application_form.is_valid():
                application_form.save()
                messages.success(request, 'Your application has been submitted successfully.')
                return redirect('all_colleges')
        else:
            form = EnquiryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Our team will contact you soon.')
                return redirect('all_colleges')
    else:
        form = EnquiryForm()
        application_form = ApplicationForm()

    notifications = Notification.objects.filter(notification_end_date__gte=timezone.now())
    clients_review = ClientReview.objects.all() 
    exam = ExamModel.objects.all()   
    colleges = CollegeModel.objects.all()
    college = CollegeModel.objects.filter(courses=course)
    course_collections = Course_Collection.objects.all()
    sub_collections = Sub_Collection.objects.all()
    sub_categories = SubCollectionCategory.objects.all()
    main_header = headerMain.objects.all()
    sub_headers = SubHeader.objects.all()
    sub_headings = SubHeaderHeading.objects.all()
    footer_colleges = CollegeModel.objects.order_by('-id')[:5]
    footer_courses = Course_Model.objects.order_by('-id')[:7]
    footer_exams = ExamModel.objects.order_by('-id')[:7]
    
    return render(request, 'course_details.html', {
        'form': form,
        'application_form':application_form,
        'colleges': colleges,
        'course': course,
        'course_collections': course_collections,
        'sub_collections': sub_collections,
        'sub_categories': sub_categories,
        'college':college,
        'clients_review':clients_review,
        'exam' : exam,
        'footer_colleges': footer_colleges,
        'footer_courses': footer_courses,
        'footer_exams': footer_exams,
        'main_header' : main_header,
        'sub_headers' : sub_headers,
        'sub_headings' : sub_headings,
        'notifications':notifications
    })


def add_on_course_details(request, id):
    course = get_object_or_404(AddOn_Course, id=id)
    
    if request.method == 'POST':
        if 'first_name' in request.POST:  # Assuming 'first_name' is unique to ApplicationForm
            application_form = ApplicationForm(request.POST)
            if application_form.is_valid():
                application = application_form.save(commit=False)
                application.course = course.course_name
                application.save()
                messages.success(request, 'Your application has been submitted successfully.')
                return redirect('add_on_course_details', id=id)
        else:
            form = EnquiryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Our team will contact you soon.')
                return redirect('add_on_course_details', id=id)
    else:
        form = EnquiryForm()
        application_form = ApplicationForm()

    # Context data
    add_on = AddOn_Course.objects.all()
    notifications = Notification.objects.filter(notification_end_date__gte=timezone.now())
    clients_review = ClientReview.objects.all() 
    exam = ExamModel.objects.all()   
    colleges = CollegeModel.objects.all()

    main_header = headerMain.objects.all()
    sub_headers = SubHeader.objects.all()
    sub_headings = SubHeaderHeading.objects.all()
    footer_colleges = CollegeModel.objects.order_by('-id')[:5]
    footer_courses = Course_Model.objects.order_by('-id')[:7]
    footer_exams = ExamModel.objects.order_by('-id')[:7]

    return render(request, 'add_on_course_details.html', {
        'form': form,
        'application_form': application_form,
        'course': course,
        'colleges': colleges,

        'add_on': add_on,
        'clients_review': clients_review,
        'exam': exam,
        'footer_colleges': footer_colleges,
        'footer_courses': footer_courses,
        'footer_exams': footer_exams,
        'main_header': main_header,
        'sub_headers': sub_headers,
        'sub_headings': sub_headings,
        'notifications': notifications
    })


def exam_detail(request, exam_name):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Our team will contact you soon.')
            return redirect('exam_detail', exam_name=exam_name)  # Redirect to the same college details page
    else:
        form = EnquiryForm()

    notifications = Notification.objects.filter(notification_end_date__gte=timezone.now())
    exam = ExamModel.objects.all()  
    courses = Course_Model.objects.all()

    main_header = headerMain.objects.all()
    sub_headers = SubHeader.objects.all()
    sub_headings = SubHeaderHeading.objects.all()
    exam = ExamModel.objects.filter(status=False)
    category = get_object_or_404(ExamModel, exam_name=exam_name, status=False)
    footer_colleges = CollegeModel.objects.order_by('-id')[:5]
    footer_courses = Course_Model.objects.order_by('-id')[:7]
    footer_exams = ExamModel.objects.order_by('-id')[:7]
    exam_details = ExamDetails.objects.filter(exam=category)
    context = {
        'form': form,
        'exam_details': exam_details,
        'category_name': category,
        'exam': exam,
        'courses': courses,

        'footer_colleges': footer_colleges,
        'footer_courses': footer_courses,
        'footer_exams': footer_exams,
        'main_header':main_header,
        'sub_headers': sub_headers,
        'sub_headings': sub_headings,
        'notifications':notifications
    }

    return render(request, "exam_detail.html", context)


def animation(request):
    return render(request,'animation.html')

def details_display(request, id):
    if request.method == 'POST':
        if 'first_name' in request.POST:  # Assuming 'first_name' is unique to ApplicationForm
            application_form = ApplicationForm(request.POST)
            if application_form.is_valid():
                application_form.save()
                messages.success(request, 'Your application has been submitted successfully.')
                return redirect('all_colleges')
        else:
            form = EnquiryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Our team will contact you soon.')
                return redirect('all_colleges')
    else:
        form = EnquiryForm()
        application_form = ApplicationForm()

    notifications = Notification.objects.filter(notification_end_date__gte=timezone.now())
    colleges = CollegeModel.objects.all()
    exam = ExamModel.objects.all() 
    courses = Course_Model.objects.all()

    footer_colleges = CollegeModel.objects.order_by('-id')[:5]
    footer_courses = Course_Model.objects.order_by('-id')[:7]
    footer_exams = ExamModel.objects.order_by('-id')[:7]

    return render(request, 'details_display.html', {'application_form':application_form,'courses':courses,'form':form,'exam':exam, 'colleges':colleges, 'footer_colleges': footer_colleges, 'footer_courses':footer_courses, 'footer_exams':footer_exams,'notifications':notifications})



def header_details(request, id):
    sub_heading = get_object_or_404(SubHeaderHeading, id=id)
    
    if request.method == 'POST':
        if 'first_name' in request.POST:  # Assuming 'first_name' is unique to ApplicationForm
            application_form = ApplicationForm(request.POST)
            if application_form.is_valid():
                application_form.save()
                messages.success(request, 'Your application has been submitted successfully.')
                return redirect('header_details', id=id)
        else:
            form = EnquiryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Our team will contact you soon.')
                return redirect('header_details', id=id)
    else:
        form = EnquiryForm()
        application_form = ApplicationForm()

    # Context data
    notifications = Notification.objects.filter(notification_end_date__gte=timezone.now())
    colleges = CollegeModel.objects.all()
    exam = ExamModel.objects.all() 
    courses = Course_Model.objects.all()
   
    main_header = headerMain.objects.all()
    sub_headers = SubHeader.objects.all()
    sub_headings = SubHeaderHeading.objects.all()
    footer_colleges = CollegeModel.objects.order_by('-id')[:5]
    footer_courses = Course_Model.objects.order_by('-id')[:7]
    footer_exams = ExamModel.objects.order_by('-id')[:7]
    data = HeaderDetails.objects.filter(sub_heading=sub_heading)

    return render(request, 'header_details.html', {
        'form': form,
        'application_form': application_form,
        'sub_heading': sub_heading,
        'courses': courses,
        
        'colleges': colleges,
        'exam': exam,
        'footer_colleges': footer_colleges,
        'footer_courses': footer_courses,
        'footer_exams': footer_exams,
        'main_header': main_header,
        'sub_headers': sub_headers,
        'sub_headings': sub_headings,
        'notifications': notifications,
        'data': data
    })




def page_404(request):
    return render(request, '404.html', status=404)

def home(request):
    
    colleges = CollegeModel.objects.all()
    clients_review = ClientReview.objects.all()
    client_logo = Client_Logo.objects.all()
    courses = Course_Model.objects.all()
    exam = ExamModel.objects.all()
    context = {
        'clients_review': clients_review,
        'client_logo': client_logo,
        'courses': courses,
        'exam' : exam
    }
    return render(request, 'index-2.html', context)



from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os

@csrf_exempt
def ckeditor_upload(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        upload = request.FILES['upload']
        file_extension = os.path.splitext(upload.name)[1].lower()
        
        # Check if the uploaded file is an image or a PDF
        if file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']:
            folder = 'images'
        elif file_extension == '.pdf':
            folder = 'pdfs'
        else:
            return JsonResponse({'uploaded': False, 'error': 'Unsupported file type.'})

        # Save the file in the appropriate folder
        file_name = default_storage.save(f'{folder}/{upload.name}', ContentFile(upload.read()))
        file_url = default_storage.url(file_name)
        return JsonResponse({
            'uploaded': True,
            'url': file_url
        })
    
    return JsonResponse({'uploaded': False, 'error': 'No file was uploaded.'})

def add_notification(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            notification = form.save(commit=False)
            # Debug: print to check the notification_end_date value
            print("Notification End Date:", notification.notification_end_date)
            notification.save()
            return redirect('notification_list')
        else:
            # Debug: print form errors if the form is not valid
            print(form.errors)
    else:
        form = NotificationForm()

    return render(request, 'admin_pages/add_notification.html', {'form': form})

def update_notification(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    if request.method == 'POST':
        form = NotificationForm(request.POST, instance=notification)
        if form.is_valid():
            form.save()
            return redirect('notification_list')
    else:
        form = NotificationForm(instance=notification)
    return render(request, 'admin_pages/update_notification.html', {'form': form})

def delete_notification(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    
    notification.delete()
    return redirect('notification_list')
    

def notification_list(request):
    notifications = Notification.objects.all().order_by('-created_at')
    return render(request, 'admin_pages/notification_list.html', {'notifications': notifications})

def notification(request):
    notifications = Notification.objects.all().order_by('-created_at')
    return render(request,'notification.html',{'notifications':notifications})



def all_colleges(request):
    if request.method == 'POST':
        if 'first_name' in request.POST:  # Assuming 'first_name' is unique to ApplicationForm
            application_form = ApplicationForm(request.POST)
            if application_form.is_valid():
                application_form.save()
                messages.success(request, 'Your application has been submitted successfully.')
                return redirect('all_colleges')
        else:
            form = EnquiryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Our team will contact you soon.')
                return redirect('all_colleges')
    else:
        form = EnquiryForm()
        application_form = ApplicationForm()

    # Filtering for Kerala State Colleges
    try:
        kerala_category = StateCategory.objects.get(state_name="Kerala")  # Fetch the Kerala state category
        colleges = CollegeModel.objects.filter(category=kerala_category)  # Filter colleges in Kerala
    except StateCategory.DoesNotExist:
        colleges = CollegeModel.objects.none()  # If no Kerala category is found, return an empty queryset

    client_logo = Client_Logo.objects.all()
    notifications = Notification.objects.all().order_by('-created_at')
    main_header = headerMain.objects.all()
    sub_headers = SubHeader.objects.all()
    sub_headings = SubHeaderHeading.objects.all()
    slider_images = SliderImage.objects.all()
    footer_colleges = CollegeModel.objects.order_by('-id')[:5]
    footer_courses = Course_Model.objects.order_by('-id')[:7]
    footer_exams = ExamModel.objects.order_by('-id')[:7]
    
    return render(request, 'all_colleges.html', {
        'client_logo': client_logo,
        'notifications': notifications,
        'colleges': colleges,  # Kerala colleges
        'main_header': main_header,
        'sub_headers': sub_headers,
        'sub_headings': sub_headings,
        'slider_images': slider_images,
        'footer_colleges': footer_colleges,
        'footer_courses': footer_courses,
        'footer_exams': footer_exams,
        'form': form,
        'application_form': application_form,
    })


from django.utils import timezone

def notification_details(request, message):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Our team will contact you soon.')
            return redirect('notification_details', message=message)  # Redirect to the same college details page
    else:
        form = EnquiryForm()
    details = get_object_or_404(Notification, message=message)
    course = Course_Model.objects.all()
    # courses = college.courses.all()

    
    colleges = CollegeModel.objects.all()
    main_header = headerMain.objects.all()
    sub_headers = SubHeader.objects.all()
    sub_headings = SubHeaderHeading.objects.all()
    
    slider_images = SliderImage.objects.all()
    footer_colleges = CollegeModel.objects.order_by('-id')[:5]
    footer_courses = Course_Model.objects.order_by('-id')[:7]
    footer_exams = ExamModel.objects.order_by('-id')[:7]
    # notifications = Notification.objects.all().order_by('-created_at')
    notifications = Notification.objects.filter(notification_end_date__gte=timezone.now())
    return render(request, 'notification_details.html', {'details': details,'form':form,'notifications':notifications,'course':course,'colleges':colleges,'main_header':main_header,'sub_headers':sub_headers,'sub_headings':sub_headings,'slider_images':slider_images,'footer_colleges':footer_colleges,'footer_courses':footer_courses,'footer_exams':footer_exams})


def application(request):
    
    if request.method == 'POST':
        application_form = ApplicationForm(request.POST)
        if application_form.is_valid():
            application_form.save()
            messages.success(request, 'Our team will contact you soon.')
            return redirect('application')
    else:
        application_form = ApplicationForm()
    
    course = Course_Model.objects.all()
    # courses = college.courses.all()
    client_logo = Client_Logo.objects.all()
    notifications = Notification.objects.all().order_by('-created_at')
    colleges = CollegeModel.objects.all()
    main_header = headerMain.objects.all()
    sub_headers = SubHeader.objects.all()
    sub_headings = SubHeaderHeading.objects.all()
    
    slider_images = SliderImage.objects.all()
    footer_colleges = CollegeModel.objects.order_by('-id')[:5]
    footer_courses = Course_Model.objects.order_by('-id')[:7]
    footer_exams = ExamModel.objects.order_by('-id')[:7]
    
    return render(request,'application.html',{'application_form':application_form,'course':course,'client_logo':client_logo,'notifications':notifications,'colleges':colleges,'main_header':main_header,'sub_headers':sub_headers,'sub_headings':sub_headings,'slider_images':slider_images,'footer_colleges':footer_colleges,'footer_courses':footer_courses,'footer_exams':footer_exams})



def course(request):
    
    return render(request, 'course.html')


def college_filter(request):
    
    state = request.GET.get('place', None)  # Get the state from query parameters
    print(f"Filtering colleges for state: '{state}'")  # Debugging output
    
    # Display all available states for debugging
    all_colleges = CollegeModel.objects.all()
    all_states = all_colleges.values_list('state', flat=True).distinct()
    print(f"Available states in database: {list(all_states)}")
    
    colleges = all_colleges  # Default to all colleges

    if state:  # If a state is provided, filter colleges based on the state
        colleges = colleges.filter(state__icontains=state.strip())
        print(f"Filtered colleges: {list(colleges)}")  # Debugging output

    notifications = Notification.objects.all().order_by('-created_at')
    main_header = headerMain.objects.all()
    sub_headers = SubHeader.objects.all()
    sub_headings = SubHeaderHeading.objects.all()
    return render(request, 'college_filter.html', {'colleges': colleges, 'notifications': notifications,'main_header':main_header,'sub_headers':sub_headers,'sub_headings':sub_headings})


    
def college_filter(request, id):
    print(f"Received ID: {id}")
    # Fetch the state category by ID
    category = get_object_or_404(StateCategory, id=id, status=False)

    # Fetch associated college details
    college_details = CollegeModel.objects.filter(category=category)

    # Other context data
    exam = ExamModel.objects.all()
    courses = Course_Model.objects.all()

    main_header = headerMain.objects.all()
    sub_headers = SubHeader.objects.all()
    sub_headings = SubHeaderHeading.objects.all()
    footer_colleges = CollegeModel.objects.order_by('-id')[:5]
    footer_courses = Course_Model.objects.order_by('-id')[:7]
    footer_exams = ExamModel.objects.order_by('-id')[:7]
    notifications = Notification.objects.filter(notification_end_date__gte=timezone.now())

    context = {
        'college_details': college_details,
        'category_name': category,
        'courses': courses,
        'exam': exam,
        'footer_colleges': footer_colleges,
        'footer_courses': footer_courses,
        'footer_exams': footer_exams,
        'main_header': main_header,
        'sub_headers': sub_headers,
        'sub_headings': sub_headings,
        'notifications': notifications
    }
    
    return render(request, "college_filter.html", context)






