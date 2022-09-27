from secrets import choice
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

class Jobs(models.Model):

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


