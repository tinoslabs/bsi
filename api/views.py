from django.shortcuts import render
from rest_framework import generics
from bsi_app.models import StateCategory,CollegeModel,ExamModel,ExamDetails, headerMain,SubHeader,SubHeaderHeading,HeaderDetails
from .serializers import StateCategorySerializer,CollegeModelSerializer,ExamModelSerializer,ExamDetailsSerializer, HeaderMainSerializer,SubHeaderSerializer,SubHeaderHeadingSerializer,HeaderDetailsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.


class statecategoryListCreate(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = StateCategory.objects.all()
    serializer_class  = StateCategorySerializer 
    
    
class CollegeModelViewSet(generics.ListCreateAPIView):
    queryset = CollegeModel.objects.all()
    serializer_class = CollegeModelSerializer
    
    
class ExamCategoryViewSet(generics.ListCreateAPIView):
    queryset = ExamModel.objects.all()
    serializer_class = ExamModelSerializer
    
    
class ExamDetailsListCreateAPIView(generics.ListCreateAPIView):
    queryset = ExamDetails.objects.all()
    serializer_class = ExamDetailsSerializer
    

class HeaderMainListCreateAPIView(generics.ListCreateAPIView):
    queryset = headerMain.objects.all()
    serializer_class = HeaderMainSerializer
    
    
class SubHeaderListCreateAPIView(generics.ListCreateAPIView):
    queryset = SubHeader.objects.all()
    serializer_class = SubHeaderSerializer
    
    
class SubHeaderHeadingListCreateAPIView(generics.ListCreateAPIView):
    queryset = SubHeaderHeading.objects.all()
    serializer_class = SubHeaderHeadingSerializer
    
    
class HeaderDetailsListCreateAPIView(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = HeaderDetails.objects.all()
    serializer_class = HeaderDetailsSerializer