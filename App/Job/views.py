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
    
    return render(request, 'Job/Home.html')

@login_required(login_url='login')
def jobs(request):
    
    return render(request, 'Job/Jobs.html') 

@login_required(login_url='login')
def profile(request):
    return render(request, 'Job/profile.html')