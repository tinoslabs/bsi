"""
URL configuration for bsi_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),

    path('user_login',views.user_login, name='user_login'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('admin_dashboard',views.admin_dashboard, name='admin_dashboard'),

    path('submit_query/',views.submit_query, name='submit_query'),
    path('chatbot_message_view',views.chatbot_message_view, name='chatbot_message_view'),
    path('delete_message/<int:id>/',views.delete_message, name='delete_message'),

    path('contact_view', views.contact_view, name='contact_view'),
    path('delete_contact/<int:id>/',views.delete_contact, name='delete_contact'),
    path('contact', views.contact, name='contact'),

    path('add_client_reviews',views.add_client_reviews, name='add_client_reviews'),
    path('view_client_reviews',views.view_client_reviews, name='view_client_reviews'),
    path('update_client_reviews/<int:id>/',views.update_client_reviews, name='update_client_reviews'),
    path('delete_client_review/<int:id>/',views.delete_client_review, name='delete_client_review'),

    path('add_blog_category',views.add_blog_category,name='add_blog_category'),
    path('view_blog_category',views.view_blog_category,name='view_blog_category'),
    path('update_blog_category/<int:id>/',views.update_blog_category,name='update_blog_category'),
    path('delete_blog_category/<int:id>/',views.delete_blog_category,name='delete_blog_category'),
    path('blog', views.blog, name='blog'),

    path('add_blog_details', views.add_blog_details, name='add_blog_details'),
    path('view_blog_details', views.view_blog_details, name='view_blog_details'),
    path('update_blog_details/<int:id>/', views.update_blog_details,name='update_blog_details'),
    path('delete_blog_details/<int:id>/', views.delete_blog_details,name='delete_blog_details'),
    path('blog_details',views.blog_details, name='blog_details'),
    path('blog_details/<str:blog_heading>/', views.blog_details,name='blog_details'),

    path('add_clients_logo', views.add_clients_logo, name='add_clients_logo'),
    path('view_clients_logo', views.view_clients_logo, name='view_clients_logo'),
    path('update_clients_logo/<int:id>/',views.update_clients_logo, name='update_clients_logo'),
    path('delete_clients_logo/<int:id>/',views.delete_clients_logo, name='delete_clients_logo'),

    path('service', views.service, name='service'),
    path('programs', views.programs, name='programs'),
    path('program_details', views.program_details, name='program_details'),
    path('about', views.about, name='about'),
    path('application', views.application, name='application'),
    path('apply', views.apply, name='apply'),

    path('create_college', views.create_college, name='create_college'),
    path('view_college', views.view_college, name='view_college'),
    path('update_college/<int:college_id>/', views.update_college, name='update_college'),
    path('delete_college/<int:college_id>/', views.delete_college, name='delete_college'),

    path('create_course',views.create_course, name='create_course'),
    path('view_course', views.view_course, name='view_course'),
    path('update_course/<int:course_id>/', views.update_course, name='update_course'),
    path('delete_course/<int:id>/', views.delete_course, name='delete_course'),

    path('create_course_collection', views.create_course_collection, name='create_course_collection'),
    path('view_course_collection',views.view_course_collection, name='view_course_collection'),
    # path('update_course_collection/<int:id>/', views.update_course_collection, name='update_course_collection'),
    # path('delete_course_collection/<int:id>/', views.delete_course_collection, name='delete_course_collection'),
    path('update_course_collection/<int:id>/', views.update_course_collection, name='update_course_collection'),
    path('delete_course_collection/<int:id>/', views.delete_course_collection, name='delete_course_collection'),

    path('load-courses/', views.load_courses, name='load_courses'),
    path('create_sub_collection/', views.create_sub_collection, name='create_sub_collection'),
    path('view_sub_collection',views.view_sub_collection,name='view_sub_collection'),
    path('update_sub_collection/<int:pk>/', views.update_sub_collection, name='update_sub_collection'),
    path('delete_sub_collection/<int:pk>/', views.delete_sub_collection, name='delete_sub_collection'),

    path('create_subcollection_category',views.create_subcollection_category,name='create_subcollection_category'),
    path('view_subcollection_category/', views.view_subcollection_category, name='view_subcollection_category'),
    path('update-subcollection-category/<int:pk>/', views.update_subcollection_category, name='update_subcollection_category'),
    path('delete_subcollection_category/<int:pk>/', views.delete_subcollection_category, name='delete_subcollection_category'),
    # path('load_sub_collections/', views.load_sub_collections, name='load_sub_collections'),

    path('card', views.card,name='card'),
    path('exam', views.exam, name='exam'),
    path('college_details/<str:college_name>/', views.college_details, name='college_details'),
   
    path('download-brochure/', views.download_brochure, name='download_brochure'),
    # path('request-brochure/', views.request_brochure, name='request_brochure'),
    # path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('enquiry_submition_view', views.enquiry_submition_view, name='enquiry_submition_view'),
    path('delete_enquiry_submition/<int:pk>/', views.delete_enquiry_submition, name='delete_enquiry_submition'),
    
    path('add_details',views.add_details,name='add_details'),
    path('view_details', views.view_details, name='view_details'),
    path('update-details/<int:pk>/', views.update_details, name='update_details'),
    path('delete_details/<int:pk>/', views.delete_details, name='delete_details'),

    path('details/<int:id>/', views.details_display, name='details_display'),

    path('animation', views.animation, name='animation'),

    path('slider',views.slider, name='slider'),

    path('create_exam', views.create_exam, name='create_exam'),
    path('view_exam', views.view_exam, name='view_exam'),
    path('update_exam/<int:id>/', views.update_exam, name='update_exam'),
    path('delete_exam/<int:id>/', views.delete_exam, name='delete_exam'),

    path('create_exam_category', views.create_exam_category, name='create_exam_category'),
    path('view_exam_category', views.view_exam_category, name='view_exam_category'),
    path('update_exam_category/<int:pk>/', views.update_exam_category, name='update_exam_category'),
    path('delete_exam_category/<int:pk>/', views.delete_exam_category, name='delete_exam_category'),
    path('create_exam_details', views.create_exam_details, name='create_exam_details'),
    path('view_exam_details', views.view_exam_details, name='view_exam_details'),
    path('update_exam_details/<int:id>/', views.update_exam_details, name='update_exam_details'),
    path('delete_exam_details/<int:id>/', views.delete_exam_details, name='delete_exam_details'),

    path('exam_detail/<int:id>/', views.exam_detail, name='exam_detail'),
    path('logo', views.logo, name='logo'),

    path('enquiry_view',views.enquiry_view, name='enquiry_view'),
    path('delete_enquiry/<int:id>/', views.delete_enquiry, name='delete_enquiry'),
    path('course_details/<int:id>/',views.course_details, name='course_details'),

    path('exam_detail/<str:exam_name>/', views.exam_detail, name='exam_detail'),
    path('demo', views.demo, name='demo'),
    path('page_404', views.page_404, name='page_404'),

    path('home', views.home, name='home'),

    path('create_about_video',views.create_about_video,name='create_about_video'),
    path('view_about_video',views.view_about_video,name='view_about_video'),
    path('update/<int:id>/', views.update_about_video, name='update_about_video'),
    path('delete/<int:id>/', views.delete_about_video, name='delete_about_video'),

    path('create-featured-colleges/', views.create_featured_colleges, name='create_featured_colleges'),
    path('view-featured-colleges/', views.view_featured_colleges, name='view_featured_colleges'),
    path('update_featured_colleges/<int:pk>/', views.update_featured_colleges, name='update_featured_colleges'),
    path('delete_featured_colleges/<int:pk>/', views.delete_featured_colleges, name='delete_featured_colleges'),
    path('notification', views.notification, name='notification'),

    

]
