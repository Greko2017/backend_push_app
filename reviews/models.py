from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# https://www.youtube.com/watch?v=sSKYEMEU-C8&t=371s
STATUS = (
    (0,"seen"),
    (1,"unseen"),
    (2,"sent")
)

# https://www.youtube.com/watch?v=m5O4sSVbzjw

class Employee(AbstractUser):
    department = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    push_token = models.CharField(max_length=200)
    push_status = models.IntegerField(choices=STATUS, default=1)
    # policy = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="employees", null=True, blank=True)
    
    
# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to="review_header_images/", blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    employees = models.ManyToManyField(Employee)
    def __str__(self):
        return self.title