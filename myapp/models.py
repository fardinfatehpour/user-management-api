from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    national_id = models.CharField(max_length=10, unique=True)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    secondary_password = models.CharField(max_length=100)
    access_level = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('user', 'User')])

    USERNAME_FIELD = 'national_id'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'password', 'secondary_password', 'access_level']

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/', blank=True, null=True)
    publish_date = models.DateField()

class NewsEvent(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

class UpcomingEvent(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
