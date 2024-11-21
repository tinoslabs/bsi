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

from ckeditor_uploader import views as ckeditor_views

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


    path('add_state_category', views.add_state_category, name='add_state_category'),
    path('view_state_category',views.view_state_category,name='view_state_category'),
    path('update_state_category/<int:id>/',views.update_state_category,name='update_state_category'),
    path('delete_state_category/<int:id>/', views.delete_state_category, name='delete_state_category'),
    
    path('create_college', views.create_college, name='create_college'),
    path('view_college', views.view_college, name='view_college'),
    path('update_college/<int:college_id>/', views.update_college, name='update_college'),
    path('delete_college/<int:college_id>/', views.delete_college, name='delete_college'),

    path('create_course',views.create_course, name='create_course'),
    path('view_course', views.view_course, name='view_course'),
    path('update_course/<int:course_id>/', views.update_course, name='update_course'),
    path('delete_course/<int:id>/', views.delete_course, name='delete_course'),

    path('exam', views.exam, name='exam'),
    path('college_details/<str:college_name>/', views.college_details, name='college_details'),
   
    path('download-brochure/', views.download_brochure, name='download_brochure'),
    path('enquiry_submition_view', views.enquiry_submition_view, name='enquiry_submition_view'),
    path('delete_enquiry_submition/<int:pk>/', views.delete_enquiry_submition, name='delete_enquiry_submition'),


    path('details/<int:id>/', views.details_display, name='details_display'),
    path('header_details/<int:id>/',views.header_details, name='header_details'),


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
    
    path('notification_list', views.notification_list, name='notification_list'),
    path('add_notification', views.add_notification, name='add_notification'),
    path('notification', views.notification, name='notification'),
    path('update_notification/<int:pk>/', views.update_notification, name='update_notification'),
    path('delete_notification/<int:pk>/', views.delete_notification, name='delete_notification'),
    
    path('create_slider/', views.create_slider, name='create_slider'),
    path('view_slider', views.view_slider, name='view_slider'),
    path('update_slider/<int:pk>/', views.update_slider, name='update_slider'),
    path('delete_slider/<int:pk>/', views.delete_slider, name='delete_slider'),

    path('ckeditor_upload/', views.ckeditor_upload, name='ckeditor_upload'),
    # path('ckeditor/upload/', views.ckeditor_views.upload, name='ckeditor_upload'),
    # path('ckeditor/browse/', views.ckeditor_views.browse, name='ckeditor_browse'),
    path('ckeditor/upload/', ckeditor_views.upload, name='ckeditor_upload'),
    path('ckeditor/browse/', ckeditor_views.browse, name='ckeditor_browse'),
    
    
    path('create_header_main', views.create_header_main, name='create_header_main'),
    path('view_header_main', views.view_header_main, name='view_header_main'),
    path('update_header_main/<int:pk>/', views.update_header_main, name='update_header_main'),
    path('delete_header_main/<int:pk>/', views.delete_header_main, name='delete_header_main'),
    
    path('create_header_main', views.create_header_main, name='create_header_main'),
    path('create_sub_header', views.create_sub_header, name='create_sub_header'),
    path('view_sub_header', views.view_sub_header, name='view_sub_header'),
    
    path('update_sub_header/<int:pk>/', views.update_sub_header, name='update_sub_header'),
    path('delete_sub_header/<int:pk>/', views.delete_sub_header, name='delete_sub_header'),
    path('create_sub_header_heading', views.create_sub_header_heading, name='create_sub_header_heading'),
    path('get-sub-headers/', views.get_sub_headers, name='get_sub_headers'),
    # path('get-subheaders/<int:main_header_id>/', views.get_subheaders, name='get_subheaders'),
    # path('get-sub-header-headings/', views.get_sub_header_headings, name='get_sub_header_headings'),
    
    path('update_sub_header_heading/<int:pk>', views.update_sub_header_heading, name='update_sub_header_heading'),
    path('delete_sub_header_heading/<int:pk>', views.delete_sub_header_heading, name='delete_sub_header_heading'),
    path('view_sub_header_heading/', views.view_sub_header_heading, name='view_sub_header_heading'),
    
    # path('add_header_details/', views.add_header_details, name='add_header_details'),
    # path('get-header-details/', views.get_header_details, name='get_header_details'),
    path('add_header_details/', views.add_header_details, name='add_header_details'),
    # path('get_header_details/', views.get_header_details, name='get_header_details'),
    path('view_header_details/', views.view_header_details, name='view_header_details'),
    path('update_header_details/<int:pk>/', views.update_header_details, name='update_header_details'),
    
    path('delete_header_details/<int:pk>/', views.delete_header_details, name='delete_header_details'),
    path('all_colleges', views.all_colleges, name='all_colleges'),
    
    # path('notification_details/<str:event_details>/', views.notification_details, name='notification_details'),
    path('notification_details/<str:message>/', views.notification_details, name='notification_details'),
    
    path('course',views.course,name='course'),
    path('create_add_on_course', views.create_add_on_course,name='create_add_on_course'),
    path('view_add_on_course',views.view_add_on_course, name='view_add_on_course'),
    path('update_add_on_course/<int:id>',views.update_add_on_course,name='update_add_on_course'),
    path('delete_add_on_course/<int:id>',views.delete_add_on_course,name='delete_add_on_course'),
    path('add_on_course_details/<int:id>/',views.add_on_course_details, name='add_on_course_details'),
    
    path('News_Letter_view',views.News_Letter_view,name='News_Letter_view'),
    path('delete_news_letter/<int:id>', views.delete_news_letter, name='delete_news_letter'),
    
    path('Application_view', views.Application_view, name='Application_view'),
    path('delete_application/<int:pk>/', views.delete_application, name='delete_application'),
    path('application', views.application, name='application'),
    
    path('search_results',views.search_results, name='search_results'),

    path('college_filter/<int:id>/', views.college_filter, name='college_filter'),

    
    
]
