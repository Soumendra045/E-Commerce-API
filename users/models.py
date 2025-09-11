from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):

    email = models.EmailField(unique=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']  # keep username required for admin.
    
    def __str__(self):
        return self.email
    
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    phone_number = models.CharField(max_length=10,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return f"profile of {self.user.email}"
