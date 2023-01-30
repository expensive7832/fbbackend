from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from .manager import customuser

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="profile")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    dateCreated = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

    objects = customuser()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        'first_name', 
        'last_name', 
        'password',
        
     ]
