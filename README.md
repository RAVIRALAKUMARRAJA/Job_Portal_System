# 🧑‍💼 KumarWorkConnect - Job Portal System

A **feature-rich Job Portal Web Application** built with Django, MySQL, and Bootstrap.  
Users can browse job listings, apply with resumes, and track their applications.  
Admins can post jobs, view applicants, and manage the platform efficiently.

---

## 🚀 Features

### 👤 User Side
- 🔐 Sign Up / Login with **email authentication**
- 📋 Browse available job listings
- 📄 View detailed job descriptions
- 📎 Apply for jobs (with resume upload)
- 👁️‍🗨️ Track job application history

### 🛠️ Admin Side
- 🧑‍💼 Post new job openings
- 📥 View job applications and download resumes
- ✅ Manage users and jobs via Django Admin Panel

### 🔒 Authentication
- Custom **email-based login system**
- "Apply Now" button is **only visible** to authenticated users

---

## 🗂️ Project Structure

job_portal/ │
 ├── job_portal/ # Project settings and URLs │ 
 ├── jobs/ # Jobs app 
 │ ├── templates/jobs/ 
 │ │ ├── job_list.html 
 │ │ ├── job_detail.html 
 │ │ ├── apply_job.html │
 ├── users/ # Users app with custom user model 
 │ ├── templates/jobs/ 
 │ │ ├── my_applications.html 
 │ │ ├── auth.html │ 
 ├── templates/ # Global templates 
 │ ├── base.html │ ├── home.html 
 │ ├── navbar.html │ ├── footer.html │
 ├── static/ # Static assets 
 │ ├── css/style.css 
 │ ├── images/ │ ├── staticfiles/ # Collected static files 
 ├── media/ # Uploaded resumes 
 │ ├── resumes/ 
 ├── venv/ # Virtual environment 
 ├── requirements.txt # Python dependencies 
 └── manage.py