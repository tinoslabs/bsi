from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import ChatMessage
from django.contrib.auth.decorators import login_required
from .models import ContactModel, ClientReview, Blog_Category, Blog_Details
from .forms import  ContactModelForm, ClientReviewForm, Blog_Category_Form, Blog_Details_Form
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
    clients_review = ClientReview.objects.all()
    return render(request,'index.html',{'clients_review':clients_review})


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