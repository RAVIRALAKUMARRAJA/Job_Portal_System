from django.contrib import admin
from .models import Job, JobApplication 

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'applicant', 'applied_on', 'status')

admin.site.register(Job)
admin.site.register(JobApplication, JobApplicationAdmin)
