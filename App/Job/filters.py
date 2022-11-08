import django_filters
from django_filters import CharFilter
from django import forms
from django.forms import ModelForm, TextInput, EmailInput

from .models import *

class JobsFilter(django_filters.FilterSet):
    note = CharFilter(field_name='title',lookup_expr='icontains')
    note = CharFilter(field_name='city',lookup_expr='icontains')
    note = CharFilter(field_name='state',lookup_expr='icontains')
    note = CharFilter(field_name='type',lookup_expr='icontains')
    
    class Meta:
        model = Job
        fields= ['title','city','state','type']
        