import django_filters
from django_filters import CharFilter

from .models import *

class JobsFilter(django_filters.FilterSet):
    note = CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = Jobs
        fields= ['city','state','country','zip_code']