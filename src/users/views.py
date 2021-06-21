from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
# Create your views here.

from . import models
from . import forms

class EmployeeCreateView(CreateView):    
    model = models.Employee
    form_class = forms.CreateEmployeeForm
    def form_valid(self, form):
        form.instance.user = self.request.user     

        return super().form_valid(form)
        
class UserCreateView(CreateView):
    model = User
    success_url = "/accounts/login/"
    template_name = "registration/registration.html"
    form_class = UserCreationForm
