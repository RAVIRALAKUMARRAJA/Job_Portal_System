from django.contrib import admin
from .models import Job, JobApplication 
from .models import SocialLink

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'applicant', 'applied_on', 'status')

admin.site.register(Job)
admin.site.register(JobApplication, JobApplicationAdmin)

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url')