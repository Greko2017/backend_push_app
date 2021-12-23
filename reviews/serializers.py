
from django.conf import settings

from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User, Group, Permission
import json
from django.contrib.contenttypes.models import ContentType

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('__all__')
        depth = 1