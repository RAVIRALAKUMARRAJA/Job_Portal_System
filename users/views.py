from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth import get_backends
from django.contrib.auth.decorators import login_required
from jobs.models import JobApplication

User = get_user_model()

def auth_view(request):
    if request.method == "POST":
        form_type = request.POST.get("form_type")

        # ✅ SIGN IN Logic
        if form_type == "signin":
            email = request.POST.get("signin_email")
            password = request.POST.get("signin_password")
            # If you're using email as USERNAME_FIELD, this is fine
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect("users:my_applications")
            else:
                print("Authentication Failed")
                messages.error(request, "Invalid credentials. Please try again.")

        # ✅ SIGN UP Logic
        elif form_type == "signup":
            name = request.POST.get("name")
            email = request.POST.get("signup_email")
            password1 = request.POST.get("signup_password1")
            password2 = request.POST.get("signup_password2")

            if password1 == password2:
                if not User.objects.filter(email=email).exists():
                    # Removed username= since CustomUser doesn't have it
                    user = User.objects.create_user(email=email, password=password1, first_name=name)
                    user.backend = get_backends()[0].__class__.__module__ + "." + get_backends()[0].__class__.__name__
                    login(request, user)  # ✅ Auto-login after signup
                    messages.success(request, "Account created successfully!")
                    return redirect("users:my_applications")
                else:
                    messages.error(request, "Email already exists. Try signing in.")
            else:
                messages.error(request, "Passwords do not match.")

    return render(request, "users/auth.html")  # Uses common auth.html in users app

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("users:auth")  # ✅ matches name in urls.py



@login_required
def my_applications_view(request):
    applications = JobApplication.objects.filter(applicant=request.user)

    accepted_count = applications.filter(status='Accepted').count()
    under_review_count = applications.filter(status='Pending').count()
    rejected_count = applications.filter(status='Rejected').count()

    context = {
        'applications': applications,
        'accepted_count': accepted_count,
        'under_review_count': under_review_count,
        'rejected_count': rejected_count,
    }
    return render(request, 'users/my_applications.html', context)

