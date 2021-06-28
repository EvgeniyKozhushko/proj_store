from django.urls import path

from carts import views

app_name = 'carts'

urlpatterns = [
    path('cart-edit/', views.CartView.as_view(),name='cart-edit'),
    path('cart-delete-good/<int:pk>', views.DeleteGoodInCartView.as_view(),name='cart-delete-good'),
    path('cart-update-good/', views.CartUpdate.as_view(),name='cart-update-good'),
    # path('author_update/<int:pk>/', cities_views.AuthorUpdateView.as_view(), name='author-update'),
    # path('author_delete/<int:pk>/', cities_views.AuthorDeleteView.as_view(), name='author-delete'),
]