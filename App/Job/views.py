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


def Signup(request):
    
    if request.method == "POST":

        form = CreateuserForm(request.POST)
        if  form.is_valid():
            form.save()
            return redirect('login')
   
    form = CreateuserForm()
    
    context = {
        'form' : form
    
    }    
    
    return render(request, 'Job/SignUp.html', context)


def User_login(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user  = authenticate(request, username=username, password=password)

        if user is not None:

            print("Hello World")
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Email or Password Incorrect')
            return redirect('login')
    
    return render(request, 'Job/SignIn.html')


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return  redirect('login')


@login_required(login_url='login')
def home(request):

    posts = Post.objects.all()
    
    if request.method == "POST":
        
        profile = UserProfile.objects.get(user=request.user)

        if 'post' in request.POST:
            desc = request.POST['description']
            post = Post.objects.create(user_profile=profile, description=desc)
            post.save()
            redirect('/')
    
    context = {
        'posts' : posts,
    }

    return render(request, 'Job/Home.html', context)

pid = 1
@login_required(login_url='login')
def jobs(request,pid):

    jobs = Job.objects.all()
    mainjob = Job.objects.get(id=pid)
    print(mainjob)
    context={
        'jobs':jobs,
        'mainjob':mainjob
    }
    
    return render(request, 'Job/Jobs.html',context) 


@login_required(login_url='login')
def profile(request):
    
    if (UserProfile.objects.get(user=request.user) is not None):
        profile = UserProfile.objects.get(user=request.user)
    else:
        profile = None
    context = {
        'profile' : profile
    }

    return render(request, 'Job/profile.html', context)


@login_required(login_url='login')
def update_profile(request, pid):

    profile = UserProfile.objects.get(id=pid)
    
    profileForm = UserProfileForm(request.POST, instance=profile)
    
    if request.method == "POST":
        profileForm = UserProfileForm(request.POST,instance=profile)

        if profileForm.is_valid():
            profileForm.save()
            return redirect('/')
    else:
        profileForm=UserProfileForm(instance=profile)
    context={
        'profileForm' : profileForm,
        
    }

    return render(request, 'Job/update_profile.html', context)

@login_required(login_url='login')
def employer_mode(request,your_jobs,add_job):
    
    context = {
        'your_jobs': your_jobs,
        'add_job': add_job,
        
    }

    return render(request,'Job/employer.html',context)

 
@login_required(login_url="login")
def add_job(request):
    form = NewJobForm()
    if(request.method=='POST'):

        form = NewJobForm(request.POST)
        profile = UserProfile.objects.get(user=request.user)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.employer = profile
            obj.save()
            
            return redirect('/')
        else:
            form = NewJobForm(request.POST)

    context = {
        'form': form
    }
    return render(request,'Job/add_job.html', context)


