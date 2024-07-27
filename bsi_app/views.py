from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import ChatMessage
from django.contrib.auth.decorators import login_required
from .models import ContactModel, ClientReview, Blog_Category, Blog_Details, Client_Logo, College_Model, Course_Model, Course_Model, Course_Collection, Sub_Collection, SubCollectionCategory, DetailsModel
from .forms import  ContactModelForm, ClientReviewForm, Blog_Category_Form, Blog_Details_Form, Client_Logo_Form, CollegeModelForm,CourseForm,CourseCollectionForm, Sub_Collection_Form, SubCollectionCategoryForm, DetailsModelForm
# Create your views here.

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


def index(request):
    colleges = College_Model.objects.all()
    clients_review = ClientReview.objects.all()
    client_logo = Client_Logo.objects.all()
    courses = Course_Model.objects.all()
    course_collections = Course_Collection.objects.all()
    sub_collections = Sub_Collection.objects.all()
    sub_categories = SubCollectionCategory.objects.all()
    details = DetailsModel.objects.all()
    blog_category = Blog_Category.objects.filter(status=0)

    context = {
        'clients_review': clients_review,
        'client_logo': client_logo,
        'courses': courses,
        'course_collections': course_collections,
        'sub_collections': sub_collections,
        'sub_categories': sub_categories,
        'colleges': colleges,
        'details' : details,
        'blog_category' : blog_category,
    }
    return render(request, 'index.html', context)


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
    contacts = ContactModel.objects.all().order_by('-id')
    return render(request,'admin_pages/contact_view.html',{'contacts':contacts})

@login_required(login_url='user_login')
def delete_contact(request,id):
    contact = ContactModel.objects.get(id=id)
    contact.delete()
    return redirect('contact_view')

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

def contact(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactModelForm()
    return render(request,'contact.html',{'form': form})


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

@login_required(login_url='user_login')
def delete_blog_details(request,id):
    blog_details = Blog_Details.objects.get(id=id)
    blog_details.delete()
    return redirect('view_blog_details')

def blog(request):
    blog_category = Blog_Category.objects.filter(status=0)
    return render(request,'blog.html',{'blog_category':blog_category})

def blog_details(request, blog_heading):
    blog = Blog_Category.objects.all()
    category = get_object_or_404(Blog_Category, blog_heading=blog_heading, status=False)
    if category:
        blog_details = Blog_Details.objects.filter(category=category, status=False)
        context = {'blog_details': blog_details, 'category_name': category,'blog':blog}
        return render(request, "blog-details.html", context)
    else:
        messages.warning(request, "No such category found")
        return render(request, 'blog-details.html')
    



# ///// College Section Start //////

@login_required(login_url='user_login')
def create_college(request):
    if request.method == 'POST':
        form = CollegeModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_college')  # Replace with your success URL
    else:
        form = CollegeModelForm()
    return render(request, 'admin_pages/create_college.html', {'form': form})

@login_required(login_url='user_login')
def view_college(request):
    colleges = College_Model.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_college.html', {'colleges': colleges})


@login_required(login_url='user_login')
def update_college(request, college_id):
    college = get_object_or_404(College_Model, id=college_id)
    if request.method == 'POST':
        form = CollegeModelForm(request.POST, request.FILES, instance=college)
        if form.is_valid():
            form.save()
            return redirect('view_college')  # Replace with your view college URL
    else:
        form = CollegeModelForm(instance=college)
    
    return render(request, 'admin_pages/update_college.html', {'form': form, 'college': college})


@login_required(login_url='user_login')
def delete_college(request, college_id):
    college = get_object_or_404(College_Model, id=college_id)
    college.delete()
    return redirect('view_college')  # Replace 'view_colleges' with your view name for viewing all colleges



# ///// Course Section Start //////
@login_required(login_url='user_login')
def create_course(request):
    college = College_Model.objects.all()
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
    college = College_Model.objects.all() 
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
def delete_course(request, course_id):
    course = get_object_or_404(Course_Model, id=course_id)
    course.delete()
    return redirect('view_course')

# ///// Course Section End //////

def load_courses(request):
    college_id = request.GET.get('college')
    courses = Course_Model.objects.filter(college_id=college_id).all()
    return JsonResponse(list(courses.values('id', 'course_name')), safe=False)



@login_required(login_url='user_login')
def create_course_collection(request):
    if request.method == 'POST':
        form = CourseCollectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create_sub_collection')
        else:
            print(form.errors)
    else:
        form = CourseCollectionForm()

    return render(request, 'admin_pages/create_course_collection.html', {'form': form})


def view_course_collection(request):
    collections = Course_Collection.objects.all()
    return render(request,'admin_pages/view_course_collection.html',{'collections':collections})


@login_required(login_url='user_login')
def update_course_collection(request, id):
    print(f"Fetching Course_Collection with id: {id}")  # Debugging statement
    collection = get_object_or_404(Course_Collection, id=id)
    print(f"Found Course_Collection: {collection}")  # Debugging statement
    
    if request.method == 'POST':
        form = CourseCollectionForm(request.POST, request.FILES, instance=collection)
        if form.is_valid():
            form.save()
            return redirect('view_course_collection')  # Replace with your view name for viewing all collections
    else:
        form = CourseCollectionForm(instance=collection)
    
    return render(request, 'admin_pages/update_course_collection.html', {'form': form, 'collection': collection})

@login_required(login_url='user_login')
def delete_course_collection(request, id):
    collection = get_object_or_404(Course_Collection, id=id)
    collection.delete()
    return redirect('view_course_collection')  # Ensure this view exists and is correctly named
    


@login_required(login_url='user_login')
def create_sub_collection(request):
    course_collections = Course_Collection.objects.all()
    if request.method == 'POST':
        form = Sub_Collection_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_subcollection_category')  # Replace 'view_courses' with your view name
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = Sub_Collection_Form()

    return render(request, 'admin_pages/create_sub_collection.html', {
        'form': form,
        'course_collections': course_collections,
    })

@login_required(login_url='user_login')
def load_courses(request):
    collection_id = request.GET.get('collection')
    if collection_id:
        try:
            course_collection = Course_Collection.objects.get(id=collection_id)
            courses = course_collection.courses.values('id', 'course_name')
            return JsonResponse(list(courses), safe=False)
        except Course_Collection.DoesNotExist:
            return JsonResponse({'error': 'Invalid Collection ID'}, status=400)
    return JsonResponse({'error': 'Invalid Collection ID'}, status=400)


@login_required(login_url='user_login')
def view_sub_collection(request):
    sub_courses = Sub_Collection.objects.select_related('course').all()
    return render(request, 'admin_pages/view_sub_collection.html', {'sub_courses': sub_courses})


@login_required(login_url='user_login')
def update_sub_collection(request, pk):
    sub_collection = get_object_or_404(Sub_Collection, pk=pk)
    if request.method == 'POST':
        form = Sub_Collection_Form(request.POST, instance=sub_collection)
        if form.is_valid():
            form.save()
            return redirect('view_sub_collections')  # Replace with your view name
    else:
        form = Sub_Collection_Form(instance=sub_collection)

    return render(request, 'admin_pages/update_sub_collection.html', {
        'form': form,
    })

@login_required(login_url='user_login')
def delete_sub_collection(request,pk):
    collections = get_object_or_404(Sub_Collection, id=pk)
    collections.delete()
    return redirect('view_sub_collection')

# @login_required(login_url='user_login')
# def create_subcollection_category(request):
#     if request.method == 'POST':
#         form = SubCollectionCategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('view_subcollection_category')  
#     else:
#         form = SubCollectionCategoryForm()

#     return render(request, 'admin_pages/create_subcollection_category.html', {'form': form})

@login_required(login_url='user_login')
def create_subcollection_category(request):
    if request.method == 'POST':
        form = SubCollectionCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_subcollection_category')  
    else:
        form = SubCollectionCategoryForm()

    return render(request, 'admin_pages/create_subcollection_category.html', {'form': form})


@login_required(login_url='user_login')
def view_subcollection_category(request):
    subcollection_categories = SubCollectionCategory.objects.all()
    return render(request, 'admin_pages/view_subcollection_category.html', {'subcollection_categories': subcollection_categories})


@login_required(login_url='user_login')
def update_subcollection_category(request, pk):
    # Fetch the existing SubCollectionCategory instance
    subcollection_category = get_object_or_404(SubCollectionCategory, pk=pk)
    
    if request.method == 'POST':
        form = SubCollectionCategoryForm(request.POST, instance=subcollection_category)
        if form.is_valid():
            form.save()
            return redirect('view_subcollection_category')  
    else:
        form = SubCollectionCategoryForm(instance=subcollection_category)
    
    return render(request, 'admin_pages/update_subcollection_category.html', {'form': form})


@login_required(login_url='user_login')
def delete_subcollection_category(request, pk):
    # Fetch the SubCollectionCategory instance to delete
    subcollection_category = get_object_or_404(SubCollectionCategory, pk=pk) 
    subcollection_category.delete()
    return redirect('view_subcollection_category')  # Redirect to a list or detail view


@login_required(login_url='user_login')
def add_details(request):
    sub_collection_categories = SubCollectionCategory.objects.all()
    if request.method == 'POST':
        form = DetailsModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_details')  # Replace 'details_list' with the name of your view that lists the details
    else:
        form = DetailsModelForm()
    
    return render(request, 'admin_pages/add_details.html', {
        'form': form,
        'sub_collection_categories': sub_collection_categories,
    })


@login_required(login_url='user_login')
def view_details(request):
    details = DetailsModel.objects.all()
    return render(request,'admin_pages/view_details.html',{'details':details})

@login_required(login_url='user_login')
def update_details(request, pk):
    details_instance = get_object_or_404(DetailsModel, pk=pk)
    sub_collection_categories = SubCollectionCategory.objects.all()
    
    if request.method == 'POST':
        form = DetailsModelForm(request.POST, instance=details_instance)
        if form.is_valid():
            form.save()
            return redirect('view_details')  # Replace 'details_list' with the name of your view that lists the details
    else:
        form = DetailsModelForm(instance=details_instance)
    return render(request, 'admin_pages/update_details.html', {
        'form': form,
        'sub_collection_categories': sub_collection_categories,
    })


@login_required(login_url='user_login')
def delete_details(request, pk):
    collection = get_object_or_404(DetailsModel, id=pk)
    collection.delete()
    return redirect('view_details') 


    
# def blog_details(request):
    
#     return render(request,'blog-details.html') 


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

def programs(request):
    return render(request,'programs.html')

def program_details(request):
    return render(request,'program-details.html')

def about(request):
    return render(request,'about.html')

def application(request):
    return render(request,'application.html')

def apply(request):
    return render(request,'apply.html')


def card(request):
    return render(request,'card.html')

def exam(request):
    return render(request,'exam.html')

# def college_details(request, college_name):
#     college = get_object_or_404(College_Model, college_name=college_name)
#     return render(request, 'college_details.html', {'college': college})

def college_details(request, college_name):
    college = get_object_or_404(College_Model, college_name=college_name)
    colleges = College_Model.objects.all()
    courses = college.courses.all()  # Fetch related courses
    return render(request, 'college_details.html', {'college': college, 'courses': courses,'colleges':colleges})

def animation(request):
    return render(request,'animation.html')


def details_display(request, id):
    sub_collection_category = get_object_or_404(SubCollectionCategory, id=id)
    data = DetailsModel.objects.filter(sub_collection_category=sub_collection_category)
    return render(request, 'details_display.html', {'data': data, 'sub_collection_category': sub_collection_category})


def course_details(request, id):
    
    data = get_object_or_404(College_Model, id=id)
    return render(request, 'course_deatils.html', {'data': data})