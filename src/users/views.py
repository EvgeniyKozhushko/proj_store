from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView, FormView
from django.contrib.auth import get_user_model, login
from django.contrib.auth.models import GroupManager


User = get_user_model()

from . import models
from . import forms

class RegisterView(FormView):
    template_name = 'users/create.html' #accounts ?
    form_class = forms.RegisterForm
    success_url = "/accounts/login/" # прописать хом!!!!
    
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        phone_number = form.cleaned_data.get('phone_number')
        email = form.cleaned_data.get('email')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        customer = models.Customer.objects.create(user=user, phone_number=phone_number)
        #customer.save()
        login(self.request, user) # проверить автологин
        return super().form_valid(form)



class EmployeeCreateView(CreateView):    
    model = models.Employee
    form_class = forms.CreateEmployeeForm
    def form_valid(self, form):
        form.instance.user = self.request.user     

        return super().form_valid(form)

class EmployeeListView(ListView):
    model = models.Employee      
    
# class UserCreateView(CreateView):
#     model = User
#     success_url = "/accounts/login/"
#     template_name = "registration/registration.html"
#     form_class = UserCreationForm

class EmployeeUpdateView(UpdateView):
    model = models.Employee
    form_class = forms.CreateEmployeeForm

class EmployeeDetailView(DetailView):
    model = models.Employee
