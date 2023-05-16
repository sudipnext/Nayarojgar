from django.urls import path
from . import views
urlpatterns =[
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.LogoutView, name="logout"),
    path("signup/company/", views.CompanySignUpView.as_view(), name="company-signup"),
    path("signup/jobfinder/", views.JobFinderSignUpView.as_view(), name="jobfinder-signup"),

]