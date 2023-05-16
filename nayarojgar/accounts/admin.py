from django.contrib import admin
from .models import Company, JobFinder, User
# Register your models here.
admin.site.register(Company)
admin.site.register(JobFinder)
admin.site.register(User)
