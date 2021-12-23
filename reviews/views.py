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
