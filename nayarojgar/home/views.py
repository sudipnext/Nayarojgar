from django.shortcuts import render, redirect
from accounts.decorators import job_seeker_required, company_required
from django.contrib.auth.decorators import login_required
from .forms import JobPostForm
from .models import JobPost

# Create your views here.

@login_required
@job_seeker_required
def jobfinder_home(request):
    posts = JobPost.objects.all()
    context = {
        'username': request.user.username,
        'posts': posts

    }
    return render(request, "home/jobfinder_home.html", context)


@login_required
@company_required
def company_home(request):
    posts = JobPost.objects.all()
    context = {
        'username': request.user.username,
        'posts': posts
    }
    return render(request, "home/company_home.html", context)


@login_required
@company_required
def jobPost(request):
    if request.method == "GET":
        context={'form': JobPostForm()}
        return render(request, "home/jobpost.html", context)
    
    elif request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company-home')
        else:
            return render(request, "home/jobpost.html", {'form': form})
        

