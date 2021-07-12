from django.urls import path
from django.contrib.auth import views as auth_views

from users import views as users_views


app_name = 'users'

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(redirect_field_name='home_books.html'), name='logout'), #система ищет нейки профайл!
    path('update-account/<int:pk>/', users_views.CustomerUpdateView.as_view(), name='update-account'),
    path('detail-account/<int:pk>/', users_views.CustomerDetailView.as_view(), name='detail-account'),

    path('register/', users_views.RegisterView.as_view(), name='register'),

    path('customer-list/', users_views.CustomerListView.as_view(), name='customer-list'),
 
    # path('create/', users_views.UserCreateView.as_view(), name='create'),
    # path('account/<int:pk>/', users_views.EmployeeDetailView.as_view(), name='account'),
    # path('account-list', users_views.EmployeeListView.as_view(), name='account-list'),


    # path('account/<str:user>', users_views.EmployeeDetailView.as_view(template_name='employee_detail.html'), name='account'),
    #path('create/', auth_views.CustomerCreateView.as_view()),
    #

]