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

    path('user_login',views.user_login,name='user_login'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),

    path('submit_query/',views.submit_query, name='submit_query'),
    path('chatbot_message_view',views.chatbot_message_view,name='chatbot_message_view'),
    path('delete_message/<int:id>/',views.delete_message,name='delete_message'),

    path('contact_view', views.contact_view, name='contact_view'),
    path('delete_contact/<int:id>/',views.delete_contact,name='delete_contact'),
    path('contact', views.contact, name='contact'),

    path('add_client_reviews',views.add_client_reviews,name='add_client_reviews'),
    path('view_client_reviews',views.view_client_reviews,name='view_client_reviews'),
    path('update_client_reviews/<int:id>/',views.update_client_reviews,name='update_client_reviews'),
    path('delete_client_review/<int:id>/',views.delete_client_review,name='delete_client_review'),

    path('add_blog_category',views.add_blog_category,name='add_blog_category'),
    path('view_blog_category',views.view_blog_category,name='view_blog_category'),
    path('update_blog_category/<int:id>/',views.update_blog_category,name='update_blog_category'),
    path('delete_blog_category/<int:id>/',views.delete_blog_category,name='delete_blog_category'),
    path('blog', views.blog, name='blog'),

    path('add_blog_details',views.add_blog_details,name='add_blog_details'),
    path('view_blog_details',views.view_blog_details,name='view_blog_details'),
    path('update_blog_details/<int:id>/',views.update_blog_details,name='update_blog_details'),
    path('delete_blog_details/<int:id>/',views.delete_blog_details,name='delete_blog_details'),
    path('blog_details',views.blog_details, name='blog_details'),
    path('blog_details/<str:blog_heading>/',views.blog_details,name='blog_details'),

    path('add_clients_logo',views.add_clients_logo,name='add_clients_logo'),
    path('view_clients_logo',views.view_clients_logo,name='view_clients_logo'),
    path('update_clients_logo/<int:id>/',views.update_clients_logo,name='update_clients_logo'),
    path('delete_clients_logo/<int:id>/',views.delete_clients_logo,name='delete_clients_logo'),

    path('service', views.service, name='service'),
    path('programs', views.programs, name='programs'),
    path('program_details', views.program_details, name='program_details'),
    path('about', views.about, name='about'),
    path('application', views.application, name='application'),
    path('apply', views.apply, name='apply'),
 
]
