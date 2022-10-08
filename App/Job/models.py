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

class UserProfile(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length = 10)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    

    def __str__(self):
        return self.first_name

class Experience(models.Model):
    job_title = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length =100)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    def __str__(self):
        return self.job_title

class Post(models.Model):
    description = models.CharField(max_length=500)
    created_at = models.DateField(default=datetime.now())
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description

class Comments(models.Model):
    comment = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentor = models.OneToOneField(UserProfile, on_delete= models.CASCADE)

    def __str__(self):
        return self.post.user_profile

class Job(models.Model):

    time = [('part-time','part-time'),('full-time','full-time'),('contract','contract')]

    job_title = models.CharField(max_length=20)
    job_description = models.CharField(max_length=100)
    employer = models.CharField(max_length = 20)
    responsibilities = models.CharField(max_length=100)
    job_type = models.CharField(max_length=10, choices= time)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    zip_code = models.IntegerField()


    def __str__(self):
        return self.job_title




@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)