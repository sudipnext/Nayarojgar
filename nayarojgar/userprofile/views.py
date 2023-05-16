from accounts.decorators import job_seeker_required, company_required
from django.contrib.auth.decorators import login_required
from accounts.models import Company, JobFinder, User
from django.shortcuts import render, get_object_or_404

# Create your views here.

@login_required(login_url='login')
def JobSeekerProfile(request, username):
    
    jobfinder = get_object_or_404(JobFinder, user__username=username)
    context={
        'data': jobfinder,
    }
    return render(request, 'userprofile/user_profile.html', context)

@login_required(login_url='login')
def CompanyProfile(request, username):
    company = get_object_or_404(Company, user__username=username)
    context={
        'comp': company,
    }
    return render(request, 'userprofile/company_profile.html', context)