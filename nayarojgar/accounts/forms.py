from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import JobFinder, Company
from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()
JOB_TYPES = [
    ('R', 'Remote'),
    ('O', 'Onsite')
]


class JobFinderSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    location = forms.CharField(widget=forms.TextInput())
    bio = forms.CharField(widget=forms.Textarea)
    contact = forms.CharField(widget=forms.TextInput())

    prefered_job_type = forms.ChoiceField(
        widget=forms.RadioSelect, choices=JobFinder.job_types)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name',
                  'last_name', 'contact', 'location', 'bio', 'prefered_job_type')

    @transaction.atomic
    def save(self, commit=True):
        # don't just commit yet
        user = super().save(commit=False)
        user.is_jobseeker = True
        if commit:
            user.save()
        jobfinder = JobFinder.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get("last_name"), contact=self.cleaned_data.get("contact"), bio=self.cleaned_data.get("bio"), location=self.cleaned_data.get("location"), prefered_job_type=self.cleaned_data.get("prefered_job_type"))
        return user


class CompanySignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    name = forms.CharField(widget=forms.TextInput())
    phone = forms.CharField(widget=forms.TextInput())
    location = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.Textarea)
    industry = forms.CharField(widget=forms.TextInput())
    website = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'name',
                  'phone', 'location', 'description', 'industry', 'website')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_company = True
        if commit:
            user.save()
        company = Company.objects.create(user=user, name=self.cleaned_data.get("name"), location=self.cleaned_data.get("location"), phone=self.cleaned_data.get(
            "phone"), description=self.cleaned_data.get("description"), industry=self.cleaned_data.get("industry"), website=self.cleaned_data.get("website"))
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.TextInput())
