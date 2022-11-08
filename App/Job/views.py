from .forms import *
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .filters import *
from . import helper



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


@login_required(login_url='login')
def jobs(request,pid):

    if request.method=="POST":

        if 'change_main_job' in request.POST:
            return redirect('/jobs/'+helper.change_main_job(request))

        if 'search_jobs' in request.POST:
            context = helper.search_jobs(request)
            return render(request,'Job/jobs.html', context)

    jobs = Job.objects.all()
    mainjob = Job.objects.get(id=pid)
    context = {
        'jobs':jobs,
        'mainjob':mainjob,
    }

    return render(request,'Job/jobs.html',context)
     

@login_required(login_url='login')
def employer_mode(request,pid):

    if request.method == "POST":
        
        if 'change_main_job' in request.POST:
            mainjob = request.POST.get("mainjob")
            return redirect('/employer/'+mainjob)

        if 'search_jobs' in request.POST:
            context = helper.search_jobs(request)
            return render(request,'Job/employer.html', context)
        
    profile = UserProfile.objects.get(user=request.user)
    jobs = Job.objects.filter(employer=profile)
    numjob = jobs.count()

    mainjob = jobs[:1]

    context={
        'numJob':numjob,
        'jobs':jobs,
        'mainjob':mainjob
    }
       
    return render(request, 'Job/employer.html',context)

 
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
    
@login_required(login_url='login')
def profile(request):
    
    if (UserProfile.objects.get(user=request.user) is not None):
        profile = UserProfile.objects.get(user=request.user)
        experiences = Experience.objects.filter(user_profile=profile)
        certificates = Certifications.objects.filter(user_profile=profile)
    
    else:
        profile = None
        experiences = None
    
    context = {
        'certificates':certificates,
        'profile' : profile,
        'experiences': experiences,
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
def add_experience(request):

    if request.method=="POST":
        form = ExperienceForm(request.POST)
        profile = UserProfile.objects.get(user=request.user)

        if form.is_valid():
            experience = form.save(commit=False)
            experience.user_profile = profile
            experience.save()
        return redirect('profile/')
        
    form = ExperienceForm()
    context = {
        'form':form,

    }
    return render(request,'Job/add_experience.html', context)

@login_required(login_url='login')
def add_certification(request):

    if request.method=="POST":
        form = CertificationForm(request.POST,request.FILES)
        profile = UserProfile.objects.get(user=request.user)

        if form.is_valid():
            certification = form.save(commit=False)
            certification.user_profile = profile
            certification.save()
        return redirect('profile/')
        
    form = CertificationForm()
    context = {
        'form':form,

    }
    return render(request,'Job/add_certification.html', context)