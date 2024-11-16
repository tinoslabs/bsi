from django.urls import path
from . import views

urlpatterns = [
    path('statecategoryListCreate/', views.statecategoryListCreate.as_view(), name='statecategoryListCreate'),
    path('CollegeModelViewSet/', views.CollegeModelViewSet.as_view(), name='CollegeModelViewSet'),
    path('ExamCategoryViewSet/', views.ExamCategoryViewSet.as_view(), name='ExamCategoryViewSet'),
    path('ExamDetailsListCreateAPIView/', views.ExamDetailsListCreateAPIView.as_view(), name='ExamDetailsListCreateAPIView'),
    path('header-main/', views.HeaderMainListCreateAPIView.as_view(), name='header-main'),
    path('sub-header/', views.SubHeaderListCreateAPIView.as_view(), name='sub-header'),
    path('subheader-heading/', views.SubHeaderHeadingListCreateAPIView.as_view(), name='subheader-heading-list-create'),
    path('header-details/', views.HeaderDetailsListCreateAPIView.as_view(), name='header-details-list-create'),
    
]
