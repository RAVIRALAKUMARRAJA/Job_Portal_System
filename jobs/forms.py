from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['resume', 'cover_letter']

class CustomSignupForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True, help_text="Full Name")

    class Meta:
        model = User
        fields = ["username", "name", "email", "password1", "password2"]