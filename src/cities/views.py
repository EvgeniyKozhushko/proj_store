from django.shortcuts import render
from django.http import HttpResponse

from . import models
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