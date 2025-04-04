from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_backends
from django.contrib.auth import get_user_model
User = get_user_model()




def auth_view(request):
    if request.method == "POST":
        form_type = request.POST.get("form_type")

        # ✅ SIGN IN Logic
        if form_type == "signin":
            email = request.POST.get("email")
            password = request.POST.get("password")

            # ✅ Authenticate user using email instead of username
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect("users:my_applications")  # Redirect to My Applications Page
            else:
                messages.error(request, "Invalid credentials. Please try again.")

        # ✅ SIGN UP Logic
        elif form_type == "signup":
            name = request.POST.get("name")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")

            if password1 == password2:
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(username=email, email=email, password=password1, first_name=name)
                    login(request, user)  # ✅ Auto-login after signup
                    messages.success(request, "Account created successfully!")
                    return redirect("users:my_applications")
                else:
                    messages.error(request, "Email already exists. Try signing in.")
            else:
                messages.error(request, "Passwords do not match.")

    return render(request, "users/auth.html")  # Uses common auth.html in job portalbs app

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("users:auth_view")  # Redirect to authentication page

def my_applications_view(request):
    return render(request, "users/my_applications.html")