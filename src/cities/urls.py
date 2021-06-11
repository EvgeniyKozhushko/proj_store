from django.urls import path

from cities import views as cities_views

app_name = 'cities'

urlpatterns = [
    path('author/<int:pk>/', cities_views.AuthorDetailView.as_view(),name='author'),
    path('author-list/', cities_views.AuthorListView.as_view(), name='author-list'),
    path('author_create/', cities_views.AuthorCreateView.as_view(), name='author-create'),
    path('author_update/<int:pk>/', cities_views.AuthorUpdateView.as_view(), name='author-update'),
    path('author_delete/<int:pk>/', cities_views.AuthorDeleteView.as_view(), name='author-delete'),

    path('series/<int:pk>/', cities_views.SeriesDetailView.as_view(), name='series'),
    path('series-list', cities_views.SeriesListView.as_view(), name='series-list'),
    path('series_create/', cities_views.SeriesCreateView.as_view(), name='series-create'),
    path('series_update/<int:pk>/', cities_views.SeriesUpdateView.as_view(), name='series-update'),
    path('series_delete/<int:pk>/', cities_views.SeriesDeleteView.as_view(), name='series-delete'),

    path('genre/<int:pk>/', cities_views.GenreDetailView.as_view(), name='genre'),
    path('genre-list/', cities_views.GenreListView.as_view(), name='genre-list'),
    path('genre_create/', cities_views.GenreCreateView.as_view(), name='genre-create'),
    path('genre_update/<int:pk>/', cities_views.GenreUpdateView.as_view(), name='genre-update'),
    path('genre_delete/<int:pk>/', cities_views.GenreDeleteView.as_view(), name='genre-delete'),

    path('published/<int:pk>/', cities_views.PublishingHouseDetailView.as_view(), name='published'),
    path('published-list/', cities_views.PublishingHouseListView.as_view(), name='published-list'),
    path('published_create/', cities_views.PublishingHouseCreateView.as_view(), name='published-create'),
    path('published_update/<int:pk>/', cities_views.PublishingHouseUpdateView.as_view(), name='published-update'),
    path('published_delete/<int:pk>/', cities_views.PublishingHouseDeleteView.as_view(), name='published-delete'),

    # path('book/<int:pk>/', cities_views.BookDetailView.as_view(), name='book'),
    # path('book-list/', cities_views.BookListView.as_view(), name='book-list'),
    # path('book_create/', cities_views.BookCreateView.as_view(), name='book-create'),
    # path('book_update/<int:pk>/', cities_views.BookUpdateView.as_view(), name='book-update'),
    # path('book_delete/<int:pk>/', cities_views.BookDeleteView.as_view(), name='book-delete'),
]