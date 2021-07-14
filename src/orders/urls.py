from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('create-order/', views.CreateOrderView.as_view(),name='create-order'),
    path('list-order/', views.ListOrderView.as_view(),name='list-order'),
    path('deteil-order/<int:pk>/', views.DetailOrderView.as_view(),name='deteil-order'),
    path('update-order/<int:pk>/', views.UpdateOrderView.as_view(),name='update-order'),
    path('customer-list-order/', views.CustomerOrderListView.as_view(),name='customer-list-order'),
    path('customer-order-update/<int:pk>/', views.CustomerUpdateOrderView.as_view(), name='customer-order-update'),
    # path('author_delete/<int:pk>/', cities_views.AuthorDeleteView.as_view(), name='author-delete'),
]