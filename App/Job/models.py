from curses.ascii import NUL
from email.policy import default
from pydoc import describe
from secrets import choice
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
from pymysql import NULL
from requests import request
from ckeditor.fields import RichTextField

class UserProfile(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20,null=True,default=None)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length = 10)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    

    def __str__(self):
        return self.first_name

class Post(models.Model):
    description = models.CharField(max_length=500)
    created_at = models.DateField()
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.description

time = [('Part-time','Part-time'),('Full-time','Full-time'),('Contract','Contract')]

class Job(models.Model):

    title = models.CharField(max_length=20)
    type = models.CharField(max_length=15, choices= time)
    street_address = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    pay_range = models.CharField(max_length=20,null=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    employer_name = models.CharField(max_length=30,null=True)
    zip_code = models.IntegerField()
    job_description = RichTextField(blank=True, null=True)
    employer = models.ForeignKey(UserProfile, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.title

class Experience(models.Model):

    job_title = models.CharField(max_length=20)
    employer = models.CharField(max_length=100)
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=time)
    job_description = RichTextField(blank=True, null=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.job_title

class Certifications(models.Model):

    certification_name = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='Job/')
    issued_by = models.CharField(max_length=100)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.certification_name


@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

