from cProfile import Profile
from pickle import FALSE
import re
from xml.etree.ElementTree import Comment
from .forms import *
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .filters import *

"""
    Helper function to search jobs on on basis of search entires.
    @param - request 
    @return - context with jobs and main_job

"""
@login_required(login_url='login')
def search_jobs(request):

    jobfilter = JobsFilter(request.POST)
    jobfilter.title = request.POST.get('title')
    jobfilter.city = request.POST.get('city')
    jobfilter.type = request.POST.get('type')
    jobs = jobfilter.qs
    mainjob = jobs[:1]
    context={
    
    'jobs':jobs,
    'mainjob':mainjob
    }

    return context


"""
    Helper function to get the job which user has selected

"""
@login_required(login_url='login')
def change_main_job(request):
    return request.POST.get("mainjob")



        
    