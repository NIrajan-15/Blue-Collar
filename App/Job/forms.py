from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
from .models import *
from django.forms import ModelForm
from django import forms


class CreateuserForm(UserCreationForm):
    username = forms.EmailField(label='Email', 
                    widget=forms.TextInput(),required=True)

    class Meta:
        model = User
        fields = ("username",  "password1", "password2")

    def save(self, commit=True):
        user = super(CreateuserForm, self).save(commit=False)
        user.email = self.cleaned_data['username']
        if commit:
            user.save()
        return user

class UserProfileForm(ModelForm):
    middle_name = forms.CharField(required=False)
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user_profile','created_at']

class JobTypeForm(forms.Form):

    job_choices = [('part-time','part-time'),('full-time','full-time'),('contract','contract')]

    job_type = forms.CharField(max_length=10, label="Job Type", widget=forms.Select(choices=job_choices) )

class NewJobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['employer']

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        exclude = ['user_profile']

class CertificationForm(ModelForm):
    class Meta:
        model = Certifications
        fields = '__all__'
        exclude = ['user_profile']

class ApplicationForm(ModelForm):
    class Meta:
        model = Applications
        fields = '__all__'
        exclude = ['application_job','applicant_profile','applied_on']    