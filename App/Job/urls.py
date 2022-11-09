from django.urls import path
from . import views
from .views import *

urlpatterns = [
    
    path('',views.home, name='home'),
    path('signup/',views.Signup,name='signup'),
    path('login/', views.User_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('jobs/<str:pid>',views.jobs, name='jobs'),
    path('updateprofile/<str:pid>/', views.update_profile, name='updateprofile'),
    path('employer/<str:pid>/',views.employer_mode, name='employer'),
    path('add_job/',views.add_job, name="addJob"),
    path('add_experience',views.add_experience, name="addExp"),
    path('add_certification',views.add_certification,name="addCertification"),
    path('apply_job/<str:pid>',views.apply_job, name='applyjob'),
    
]
