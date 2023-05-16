from django.urls import path
from . import views
urlpatterns = [
    path("company/", views.company_home, name="company-home"),
    path("", views.jobfinder_home, name="jobfinder-home"),
    path("postjob/", views.jobPost, name="jobpost"),
]
