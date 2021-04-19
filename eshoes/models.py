from django.db import models
from django.db import migrations

# Create your models here.
class Jordan(models.Model):
    image_url = models.TextField(default='N/A')
    name = models.CharField(max_length=100, default='N/A')
    price = models.CharField(max_length=100, default='N/A')

    def __str__(self):
        return self.name


class Puma(models.Model):
    image_url = models.TextField(default='N/A')
    name = models.CharField(max_length=100, default='N/A')
    price = models.CharField(max_length=100, default='N/A')

    def __str__(self):
        return self.name


class Nike(models.Model):
    image_url = models.TextField(default='N/A')
    name = models.CharField(max_length=100, default='N/A')
    price = models.CharField(max_length=100, default='N/A')

    def __str__(self):
        return self.name
