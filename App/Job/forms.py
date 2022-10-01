from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
from django import forms


class CreateuserForm(UserCreationForm):
    username = forms.EmailField(label='Email', 
                    widget=forms.TextInput(attrs={'placeholder': 'Email'}),required=True)

    class Meta:
        model = User
        fields = ("username",  "password1", "password2")

    def save(self, commit=True):
        user = super(CreateuserForm, self).save(commit=False)
        user.email = self.cleaned_data['username']
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class meta:
        model = models.UserProfile
        fields = '__all__'

class JobTypeForm(forms.Form):

    job_choices = [('part-time','part-time'),('full-time','full-time'),('contract','contract')]

    job_type = forms.CharField(max_length=10, label="Job Type", widget=forms.Select(choices=job_choices) )