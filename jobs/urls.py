from django.contrib import admin

from django.urls import path,include
from . import views

app_name = 'jobs'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('job_list/', views.job_list, name='job_list'),
    path('job_detail/<int:job_id>/', views.job_detail, name='job_detail'),
    path('apply_job/<int:job_id>/', views.apply_job, name='apply_job'),
]

