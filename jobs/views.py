from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Job
from .forms import JobApplicationForm  
from .models import JobApplication  
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')


def job_list(request):
    jobs = Job.objects.all()  # Fetch all jobs from the database
    return render(request, 'jobs/job_list.html', {'jobs': jobs}) 


def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)  # Fetch job details
    return render(request, 'jobs/job_detail.html', {'job': job})  # Ensure correct template path



def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    if request.method == "POST":
        form = JobApplicationForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user  # Associate application with logged-in user
            application.save()
            return redirect('jobs:job_list')  # Redirect to job list after applying

    else:
        form = JobApplicationForm()

    return render(request, 'jobs/apply_job.html', {'job': job, 'form': form})


@login_required
def my_applications(request):
    applications = JobApplication.objects.filter(user=request.user)  # Fetch applications for logged-in user
    return render(request, 'jobs/my_applications.html', {'my_applications': my_applications})



