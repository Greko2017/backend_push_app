# Create your views here.

from .serializers import *
from .models import *
from rest_framework import viewsets, permissions
# Create your views here.

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-id')

    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all().order_by('-id')

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('-id')

    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.all().order_by('-id')
        
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all().order_by('-id')

    serializer_class = StatusSerializer

    def get_queryset(self):
        return Status.objects.all().order_by('-id')
