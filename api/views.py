from django.shortcuts import render
from rest_framework import generics
from bsi_app.models import StateCategory,CollegeModel,ExamModel,ExamDetails, headerMain,SubHeader,SubHeaderHeading,HeaderDetails,Notification
from .serializers import StateCategorySerializer,CollegeModelSerializer,ExamModelSerializer,ExamDetailsSerializer, HeaderMainSerializer,SubHeaderSerializer,SubHeaderHeadingSerializer,HeaderDetailsSerializer,NotificationSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet


# Create your views here.



    
class StateCategoryViewSet(ReadOnlyModelViewSet):
    """
    A read-only viewset for viewing StateCategory instances.
    """
    queryset = StateCategory.objects.all()
    serializer_class = StateCategorySerializer
    
    
class CollegeModelViewSet(ReadOnlyModelViewSet):
    queryset = CollegeModel.objects.all()
    serializer_class = CollegeModelSerializer
    
    
class ExamCategoryViewSet(ReadOnlyModelViewSet):
    queryset = ExamModel.objects.all()
    serializer_class = ExamModelSerializer
    
    
class ExamDetailsViewSet(ReadOnlyModelViewSet):
    queryset = ExamDetails.objects.all()
    serializer_class = ExamDetailsSerializer
    

class HeaderMainViewSet(ReadOnlyModelViewSet):
    queryset = headerMain.objects.all()
    serializer_class = HeaderMainSerializer
    
    
class SubHeaderViewSet(ReadOnlyModelViewSet):
    queryset = SubHeader.objects.all()
    serializer_class = SubHeaderSerializer
    
    
class SubHeaderHeadingViewSet(ReadOnlyModelViewSet):
    queryset = SubHeaderHeading.objects.all()
    serializer_class = SubHeaderHeadingSerializer
    
    
class HeaderDetailsViewSet(ReadOnlyModelViewSet):
    queryset = HeaderDetails.objects.all()
    serializer_class = HeaderDetailsSerializer
    
    
class NotificationViewSet(ReadOnlyModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer