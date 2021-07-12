from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from . import models
from . import forms

# Create your views here.

class Home(TemplateView):
    template_name = 'catalogs/home.html'

class CrewPage(TemplateView):
    template_name = 'catalogs/crew_page.html'
  
#Author
class AuthorDetailView(DetailView):
    model = models.Author

class AuthorListView(ListView):
    model = models.Author

class AuthorCreateView(CreateView):
    model = models.Author
    form_class = forms.CreateAuthorForm

class AuthorUpdateView(UpdateView):
    model = models.Author
    form_class = forms.CreateAuthorForm

class AuthorDeleteView(DeleteView):
    model = models.Author
    success_url = reverse_lazy('author:author-list')    

#Series
class SeriesDetailView(DetailView):
    model = models.Series

class SeriesListView(ListView):
    model = models.Series

class SeriesCreateView(CreateView):
    model = models.Series
    form_class = forms.CreateSeriesForm
    #fields = ('dim_2', 'series_discription')

class SeriesUpdateView(UpdateView):
    model = models.Series
    form_class = forms.CreateSeriesForm

class SeriesDeleteView(DeleteView):
    model = models.Series
    success_url = reverse_lazy('series:series-list')    

#Genre
class GenreDetailView(DetailView):
    model = models.Genre

class GenreListView(ListView):
    model = models.Genre    

class GenreCreateView(CreateView):
    model = models.Genre
    form_class = forms.CreateGenreForm

class GenreUpdateView(UpdateView):
    model = models.Genre
    form_class = forms.CreateGenreForm

class GenreDeleteView(DeleteView):
    model = models.Genre
    success_url = reverse_lazy('genre:genre-list') 

#Publishing House   
class PublishingHouseDetailView(DetailView):
    model = models.PublishingHouse

class PublishingHouseListView(ListView):
    model = models.PublishingHouse   

class PublishingHouseCreateView(CreateView):
    model = models.PublishingHouse
    form_class = forms.CreatePublishingHouseForm

class PublishingHouseUpdateView(UpdateView):
    model = models.PublishingHouse
    form_class = forms.CreatePublishingHouseForm

class PublishingHouseDeleteView(DeleteView):
    model = models.PublishingHouse
    success_url = reverse_lazy('publishinghouse:published-list')