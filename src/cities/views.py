from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from . import models
from . import forms

# Create your views here.

AIRPORTS = {
    'MSQ' : 'Minsk',
    'KBP' : 'Kiev',
    'IEV' : 'Kiev',
    'DME' : 'Moscow',
    'SVO' : 'Moscow',
    'VKO' : 'Moscow',
    'WAW' : 'Warsaw',
    'WMI' : 'Warsaw',
    'VNO' : 'Vilnius',
    'KUN' : 'Kaunas',
    'PLQ' : 'Palanga',
    'RIX' : 'Riga',
    'LED' : 'St.Petersburg',
    'SXF' : 'Berlin',
    'TXL' : 'Berlin',
    'CDG' : 'Paris',
    'BVA' : 'Paris',
    'ORY' : 'Paris',
    'BCN' : 'Barcelona',
    'ATH' : 'Athens',
}

def cities(request, airport):
    city = AIRPORTS.get(airport.upper(), 'City not found')
    ctx = {
        'city' : city
    }
    return render(request, template_name ="cities.html", context = ctx)

def cities_home(request):
    return render(request, template_name ="home.html", context = {})

def author(request, author_id):
    author = models.Author.objects.get(pk=author_id)
    ctx = {
        'author' : author
    }
    return render(request, template_name ="author.html", context = ctx)

def book_author_list(request):
    book_author = models.Author.objects.all()
    ctx = {
        'book_author' : book_author
    }
    return render(request, template_name ="book_author_list.html", context = ctx)

def series(request, series_id):
    series = models.Series.objects.get(pk=series_id)
    ctx = {
        'series' : series
    }
    return render(request, template_name ="series.html", context = ctx)

def book_series_list(request):
    book_series = models.Series.objects.all()
    ctx = {
        'book_series' : book_series
    }
    return render(request, template_name ="series_list.html", context = ctx)      

def genre(request, genre_id):
    genre = models.Genre.objects.get(pk=genre_id)
    ctx = {
        'genre' : genre
    }
    return render(request, template_name ="genre.html", context = ctx)

def book_genre_list(request):
    genre_list = models.Genre.objects.all()
    ctx = {
        'book_genre' : genre_list
    }
    return render(request, template_name ="genre_list.html", context = ctx)  

def published(request, published_id):
    published = models.PublishingHouse.objects.get(pk=published_id)
    ctx = {
        'published' : published
    }
    return render(request, template_name ="published.html", context = ctx)

def book_published_list(request):
    published_list = models.PublishingHouse.objects.all()
    ctx = {
        'published_list' : published_list
    }
    return render(request, template_name ="published_list.html", context = ctx)  

def author_create(request):
    if request.method == 'POST':
        form = forms.CreateAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(viewname='authors-list'))
        
    else:
        form = forms.CreateAuthorForm()
    ctx = {
        'form' : form,
        'is_valid':form.is_valid()
    }
    return render(request, template_name ="author_create.html", context = ctx)  

def author_update(request, author_id):
    if request.method == 'POST':
        obj = models.Author.objects.get(pk=author_id)
        form = forms.CreateAuthorForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(viewname='authors-list'))
        
    else:
        obj = models.Author.objects.get(pk=author_id)
        form = forms.CreateAuthorForm(instance=obj)
    ctx = {
        'form' : form,
        'is_valid':form.is_valid()
    }
    return render(request, template_name ="author_create.html", context = ctx)    

def author_delete(request, author_id):
    if request.method == 'POST':
        obj = models.Author.objects.get(pk=author_id).delete()
        return HttpResponseRedirect(reverse(viewname='authors-list'))

    return render(request, template_name ="author_delete.html", context = {})

def series_create(request):
    if request.method == 'POST':
        form = forms.CreateSeriesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(viewname='serisess-list'))
        
    else:
        form = forms.CreateSeriesForm()
    ctx = {
        'form' : form,
        'is_valid':form.is_valid()
    }
    return render(request, template_name ="series_create.html", context = ctx)  

def series_update(request, series_id):
    if request.method == 'POST':
        obj = models.Series.objects.get(pk=series_id)
        form = forms.CreateSeriesForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(viewname='serisess-list'))
        
    else:
        obj = models.Series.objects.get(pk=series_id)
        form = forms.CreateSeriesForm(instance=obj)
    ctx = {
        'form' : form,
        'is_valid':form.is_valid()
    }
    return render(request, template_name ="series_create.html", context = ctx)    

def series_delete(request, series_id):
    if request.method == 'POST':
        obj = models.Series.objects.get(pk=series_id).delete()
        return HttpResponseRedirect(reverse(viewname='serisess-list'))

    return render(request, template_name ="series_delete.html", context = {})

def genre_create(request):
    if request.method == 'POST':
        form = forms.CreateGenreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(viewname='genres-list'))
        
    else:
        form = forms.CreateGenreForm()
    ctx = {
        'form' : form,
        'is_valid':form.is_valid()
    }
    return render(request, template_name ="genre_create.html", context = ctx)  

def genre_update(request, genre_id):
    if request.method == 'POST':
        obj = models.Genre.objects.get(pk=genre_id)
        form = forms.CreateGenreForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(viewname='genres-list'))
        
    else:
        obj = models.Genre.objects.get(pk=genre_id)
        form = forms.CreateGenreForm(instance=obj)
    ctx = {
        'form' : form,
        'is_valid':form.is_valid()
    }
    return render(request, template_name ="genre_create.html", context = ctx)    

def genre_delete(request, genre_id):
    if request.method == 'POST':
        obj = models.Genre.objects.get(pk=genre_id).delete()
        return HttpResponseRedirect(reverse(viewname='genres-list'))

    return render(request, template_name ="genre_delete.html", context = {}) 

def published_create(request):
    if request.method == 'POST':
        form = forms.CreatePublishingHouseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(viewname='published-list'))
        
    else:
        form = forms.CreatePublishingHouseForm()
    ctx = {
        'form' : form,
        'is_valid':form.is_valid()
    }
    return render(request, template_name ="published_create.html", context = ctx)  

def published_update(request, published_id):
    if request.method == 'POST':
        obj = models.PublishingHouse.objects.get(pk=published_id)
        form = forms.CreatePublishingHouseForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(viewname='published-list'))
        
    else:
        obj = models.PublishingHouse.objects.get(pk=published_id)
        form = forms.CreatePublishingHouseForm(instance=obj)
    ctx = {
        'form' : form,
        'is_valid':form.is_valid()
    }
    return render(request, template_name ="published_create.html", context = ctx)    

def published_delete(request, published_id):
    if request.method == 'POST':
        obj = models.PublishingHouse.objects.get(pk=published_id).delete()
        return HttpResponseRedirect(reverse(viewname='published-list'))

    return render(request, template_name ="published_delete.html", context = {})     