from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
# Create your views here.

from . import models
from . import forms

# class CustomerCreateView(UserCreationForm):
#     model = models.Customer
#     form_class = forms.CreateCustomerForm
    # login_url = 'accounts:login'
    # permission_required = 'books.add_book'

# class MyUserCreateView(CreateView):
#     model = models.MyUser
#     form_class = forms.CreateMyUserForm


class EmployeeCreateView(CreateView):
    model = models.Employee
    form_class = forms.CreateEmployeeForm

    def get_object(self, queryset=None):
        username = models.User.objects.get(self.request.user.username)
        return username
        

class UserCreateView(CreateView):
    model = User
    success_url = "/accounts/login/"
    template_name = "registration/registration.html"
    form_class = UserCreationForm
