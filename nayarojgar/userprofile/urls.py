from django.urls import path
from . import views

urlpatterns = [
    path("profile/<str:username>/",views.JobSeekerProfile, name="userprofile"),
    path("company/<str:username>/",views.CompanyProfile, name="comp")

]