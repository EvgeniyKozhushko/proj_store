from django.core import paginator
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from django.core.paginator import Paginator

from . import models
from . import forms

# Create your views here.

class BookDetailView(DetailView):
    model = models.Book
class BookListView(ListView):
    model = models.Book
    paginate_by = 3

    def get_queryset(self):
        qs = super().get_queryset()
        filter = self.request.GET.get('filter')
        q = self.request.GET.get('q')
        print(q)
        if q:
            # qs.filter(title_book__icontains=q)
            qs = qs.filter(Q(title_book__icontains=q) | Q(book_author__dim_1__icontains=q))
        return qs


class CrewBookListView(ListView):
    model = models.Book
    template_name = 'books/crewbook_list.html'
    paginate_by = 10
    def get_queryset(self):
        qs = super().get_queryset()
        filter = self.request.GET.get('filter')
        q = self.request.GET.get('q')
        print(q)
        if q:
            # qs.filter(title_book__icontains=q)
            qs = qs.filter(Q(title_book__icontains=q) | Q(book_author__dim_1__icontains=q))
        return qs        

class HomeBookListView(ListView):
    model = models.Book
    template_name = 'books/home_books.html'
    paginate_by = 2
    def get_queryset(self):
        qs = super().get_queryset()
        filter = self.request.GET.get('filter')
        q = self.request.GET.get('q')
        print(q)
        if q:
            qs = qs.filter(Q(title_book__icontains=q) | Q(book_author__dim_1__icontains=q))
        return qs     


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
    success_url = reverse_lazy('books:book-list-crew') 
    login_url = 'accounts:login'
    permission_required = 'books.delete_book'