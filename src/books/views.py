from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from . import models
from . import forms

# Create your views here.

class Home(TemplateView):
    template_name = 'cities/home.html'

class BookDetailView(DetailView):
    model = models.Book

class BookListView(ListView):
    model = models.Book

class BookCreateView(CreateView):
    model = models.Book
    form_class = forms.CreateBookForm

class BookUpdateView(UpdateView):
    model = models.Book
    form_class = forms.CreateBookForm

class BookDeleteView(DeleteView):
    model = models.Book
    success_url = reverse_lazy('books:book-list')   