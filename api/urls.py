from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StateCategoryViewSet,CollegeModelViewSet,ExamCategoryViewSet,ExamDetailsViewSet,HeaderMainViewSet,SubHeaderViewSet,SubHeaderHeadingViewSet,HeaderDetailsViewSet,NotificationViewSet

# Create a router and register the StateCategoryViewSet
router = DefaultRouter()
router.register(r'statecategory', StateCategoryViewSet, basename='statecategory')
router.register(r'college', CollegeModelViewSet, basename='college')
router.register(r'exam-category', ExamCategoryViewSet, basename='exam-category')
router.register(r'exam-details', ExamDetailsViewSet, basename='exam-details')
router.register(r'header-main', HeaderMainViewSet, basename='header-main')
router.register(r'sub-header', SubHeaderViewSet, basename='sub-header')
router.register(r'subheader-heading', SubHeaderHeadingViewSet, basename='subheader-heading')
router.register(r'header-details', HeaderDetailsViewSet, basename='header-details')
router.register(r'notifications', NotificationViewSet, basename='notifications')

urlpatterns = [   
    path('', include(router.urls)),  # DefaultRouter-generated endpoints
]