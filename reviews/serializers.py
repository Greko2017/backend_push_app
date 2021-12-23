
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


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id',
            'email',
            'first_name',
            'username',
            'last_name',
            'groups',
            'user_permissions',
            'push_token',
        )  #'username'
        depth = 1