from django.urls import path
from .views import auth_view, logout_user,my_applications_view

app_name = "users"

urlpatterns = [
    path("auth/", auth_view, name="auth"),   # Sign-in & Sign-up
    path("logout/", logout_user, name="logout"),  # Logout
    path("my-applications/", my_applications_view, name="my_applications"),
]
