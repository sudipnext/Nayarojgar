from django.shortcuts import render, redirect
from .models import User
from .decorators import company_required, job_seeker_required
from .forms import JobFinderSignUpForm, CompanySignUpForm, LoginForm
from django.contrib.auth import login, logout
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.contrib.auth.decorators import login_required


class JobFinderSignUpView(CreateView):
    model = User
    form_class = JobFinderSignUpForm
    template_name = "accounts/jobfinder_signup.html"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'jobfinder'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("jobfinder-home")

class CompanySignUpView(CreateView):
    model = User
    form_class = CompanySignUpForm
    template_name = "accounts/company_signup.html"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("company-home")
    
def LogoutView(request):
    logout(request)
    return redirect('login')


class LoginView(LoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_company:
                return reverse('company-home')
            elif user.is_jobseeker:
                return reverse('jobfinder-home')
        else:
            return reverse('login')

