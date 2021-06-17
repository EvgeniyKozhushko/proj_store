from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from . import models
from . import forms

# Create your views here.

class Home(TemplateView):
    template_name = 'cities/home.html'

class BookDetailView(DetailView):
    model = models.Book

class BookListView(ListView):
    model = models.Book

class BookCreateView(PermissionRequiredMixin, CreateView):
    model = models.Book
    form_class = forms.CreateBookForm
    login_url = 'accounts:login'
    permission_required = 'books.add_book'

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = models.Book
    form_class = forms.CreateBookForm
    login_url = 'accounts:login'
    permission_required = 'books.change_book'
    

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = models.Book
    success_url = reverse_lazy('books:book-list') 
    login_url = 'accounts:login'
    permission_required = 'books.delete_book'