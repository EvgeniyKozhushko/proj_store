from django.urls import path

from catalogs import views as catalogs_views

app_name = 'catalogs'

urlpatterns = [
    path('author/<int:pk>/', catalogs_views.AuthorDetailView.as_view(),name='author'),
    path('author-list/', catalogs_views.AuthorListView.as_view(), name='author-list'),
    path('author_create/', catalogs_views.AuthorCreateView.as_view(), name='author-create'),
    path('author_update/<int:pk>/', catalogs_views.AuthorUpdateView.as_view(), name='author-update'),
    path('author_delete/<int:pk>/', catalogs_views.AuthorDeleteView.as_view(), name='author-delete'),

    path('series/<int:pk>/', catalogs_views.SeriesDetailView.as_view(), name='series'),
    path('series-list', catalogs_views.SeriesListView.as_view(), name='series-list'),
    path('series_create/', catalogs_views.SeriesCreateView.as_view(), name='series-create'),
    path('series_update/<int:pk>/', catalogs_views.SeriesUpdateView.as_view(), name='series-update'),
    path('series_delete/<int:pk>/', catalogs_views.SeriesDeleteView.as_view(), name='series-delete'),

    path('genre/<int:pk>/', catalogs_views.GenreDetailView.as_view(), name='genre'),
    path('genre-list/', catalogs_views.GenreListView.as_view(), name='genre-list'),
    path('genre_create/', catalogs_views.GenreCreateView.as_view(), name='genre-create'),
    path('genre_update/<int:pk>/', catalogs_views.GenreUpdateView.as_view(), name='genre-update'),
    path('genre_delete/<int:pk>/', catalogs_views.GenreDeleteView.as_view(), name='genre-delete'),

    path('published/<int:pk>/', catalogs_views.PublishingHouseDetailView.as_view(), name='published'),
    path('published-list/', catalogs_views.PublishingHouseListView.as_view(), name='published-list'),
    path('published_create/', catalogs_views.PublishingHouseCreateView.as_view(), name='published-create'),
    path('published_update/<int:pk>/', catalogs_views.PublishingHouseUpdateView.as_view(), name='published-update'),
    path('published_delete/<int:pk>/', catalogs_views.PublishingHouseDeleteView.as_view(), name='published-delete'),

]