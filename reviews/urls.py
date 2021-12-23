# from django.urls import path, include
from .views import *
# from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('review', ReviewViewSet, 'review')
router.register('employee', EmployeeViewSet, 'employee')


urlpatterns = router.urls

urlpatterns += [
    # path('number_of_customer/', views.number_of_customer),
]

CORS_ORIGIN_WHITELIST = [
    'http://localhost:19006',
    'http://localhost:3000',
]
