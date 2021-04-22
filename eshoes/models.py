from django.db import models
from django.db import migrations
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(verbose_name='email',
                              max_length=255, unique=True)
    avatar = models.CharField(max_length=500)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
        
class Jordan(models.Model):
    image_url = models.TextField(default='N/A')
    name = models.CharField(max_length=100, default='N/A')
    price = models.CharField(max_length=100, default='N/A')
    description = models.CharField(max_length=300, default='N/A')

    def __str__(self):
        return self.name


class Puma(models.Model):
    image_url = models.TextField(default='N/A')
    name = models.CharField(max_length=100, default='N/A')
    price = models.CharField(max_length=100, default='N/A')
    description = models.CharField(max_length=300, default='N/A')

    def __str__(self):
        return self.name


class Nike(models.Model):
    image_url = models.TextField(default='N/A')
    name = models.CharField(max_length=100, default='N/A')
    price = models.CharField(max_length=100, default='N/A')
    description = models.CharField(max_length=300, default='N/A')

    def __str__(self):
        return self.name
