from django.db import models
from accounts.models import Company, JobFinder

# Create your models here.


class JobPost(models.Model):
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    job_types = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    ]
    job_type = models.CharField(
        max_length=20, choices=job_types, default='full_time')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# for person or user job apply model

class JobApply(models.Model):
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    user = models.ForeignKey(JobFinder, on_delete=models.CASCADE)
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_post.title
    
    class Meta:
        verbose_name_plural = "JobApply"
