"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from cities import views as cities_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/<int:author_id>/', cities_views.author),
    path('authors', cities_views.book_author_list),

    path('series/<int:series_id>/', cities_views.series),
    path('seriess', cities_views.book_series_list),

    path('genre/<int:genre_id>/', cities_views.genre),
    path('genres', cities_views.book_genre_list),

    path('published/<int:published_id>/', cities_views.published),
    path('published_houses', cities_views.book_published_list),

    path('<str:airport>/', cities_views.cities),
    path('', cities_views.cities_home),
]