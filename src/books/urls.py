from django.urls import path

from books import views as books_views

app_name = 'books'

urlpatterns = [

    path('book/<int:pk>/', books_views.BookDetailView.as_view(), name='book'),
    path('book-list/', books_views.BookListView.as_view(), name='book-list'),
    path('book-list-crew/', books_views.CrewBookListView.as_view(), name='book-list-crew'),
    path('home-books/', books_views.HomeBookListView.as_view(), name='home-books'),
    path('book_create/', books_views.BookCreateView.as_view(), name='book-create'),
    path('book_update/<int:pk>/', books_views.BookUpdateView.as_view(), name='book-update'),
    path('book_delete/<int:pk>/', books_views.BookDeleteView.as_view(), name='book-delete'),
]