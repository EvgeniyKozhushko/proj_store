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

class EmployeeListView(ListView):
    model = models.Employee      
    
class UserCreateView(CreateView):
    model = User
    success_url = "/accounts/login/"
    template_name = "registration/registration.html"
    form_class = UserCreationForm

class EmployeeUpdateView(UpdateView):
    model = models.Employee
    form_class = forms.CreateEmployeeForm

class EmployeeDetailView(DetailView):
    model = models.Employee

# def get_context_data(self, **kwargs):
#     context = super(EmployeeDetailView, self).get_context_data(**kwargs)
#     context['employee'] = Employee.objects.get(pk=pk)
#     return context