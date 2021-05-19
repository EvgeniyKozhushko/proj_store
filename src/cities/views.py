from django.shortcuts import render
from django.http import HttpResponse

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