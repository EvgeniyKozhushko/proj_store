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
    path('author/<int:author_id>/', cities_views.author,name='author'),
    path('authors', cities_views.book_author_list, name='authors-list'),

    path('series/<int:series_id>/', cities_views.series, name='series'),
    path('seriess', cities_views.book_series_list, name='serisess-list'),

    path('genre/<int:genre_id>/', cities_views.genre, name='genre'),
    path('genres', cities_views.book_genre_list, name='genres-list'),

    path('published/<int:published_id>/', cities_views.published, name='published'),
    path('published_houses', cities_views.book_published_list, name='published-list'),

    path('author_create/', cities_views.author_create, name='author-create'),
    path('author_update/<int:author_id>/', cities_views.author_update, name='author-update'),
    path('author_delete/<int:author_id>/', cities_views.author_delete, name='author-delete'),

    path('series_create/', cities_views.series_create, name='series-create'),
    path('series_update/<int:series_id>/', cities_views.series_update, name='series-update'),
    path('series_delete/<int:series_id>/', cities_views.series_delete, name='series-delete'),

    path('genre_create/', cities_views.genre_create, name='genre-create'),
    path('genre_update/<int:genre_id>/', cities_views.genre_update, name='genre-update'),
    path('genre_delete/<int:genre_id>/', cities_views.genre_delete, name='genre-delete'),

    path('published_create/', cities_views.published_create, name='published-create'),
    path('published_update/<int:published_id>/', cities_views.published_update, name='published-update'),
    path('published_delete/<int:published_id>/', cities_views.published_delete, name='published-delete'),

    path('<str:airport>/', cities_views.cities),
    path('', cities_views.cities_home, name='home'),
]