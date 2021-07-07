from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('create-order/', views.CreateOrderView.as_view(),name='create-order'),
    path('list-order/', views.ListOrderView.as_view(),name='list-order'),
    # path('cart-update-good/', views.CartUpdate.as_view(),name='cart-update-good'),
    # path('author_update/<int:pk>/', cities_views.AuthorUpdateView.as_view(), name='author-update'),
    # path('author_delete/<int:pk>/', cities_views.AuthorDeleteView.as_view(), name='author-delete'),
]