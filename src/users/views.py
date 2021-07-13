from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
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


class CustomerUpdateView(UpdateView):
    model = models.Customer
    template_name='users/update_form.html'
    form_class = forms.CustomerUpdateForm
    def get_object(self):
        username = self.model.objects.get(user__username=self.request.user.username)
        # print(username)
        return username
    # def form_valid(self, form):
    #     form.instance.user = self.request.user     

    #     return super().form_valid(form)

class CustomerDetailView(DetailView):
    model = models.Customer
    def get_object(self):
        username = self.model.objects.get(user__username=self.request.user.username)
        # username = self.model.objects.get(user__username=self.request.user.username)
        return username

class CustomerListView(ListView):
    model = models.Customer