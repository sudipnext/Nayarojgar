from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


# Create your models here.

# created and modified the user from abstract user
class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_company = models.BooleanField(default=False)
    is_jobseeker = models.BooleanField(default=False)


class JobFinder(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="jobfinder")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=255)
    location = models.CharField(max_length=200)
    bio = models.TextField()
    job_types = [
        ('R', 'Remote'),
        ('O', 'Onsite')
    ]
    prefered_job_type = models.CharField(max_length=1, choices=job_types)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.first_name + " " + self.last_name



class Company(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="company")
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    # logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    description = models.TextField()
    industry = models.CharField(max_length=100)
    website = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=now)
    class Meta:
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name
