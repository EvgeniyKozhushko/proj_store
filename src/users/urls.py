from django.urls import path
from django.contrib.auth import views as auth_views

from users import views as users_views


app_name = 'users'

urlpatterns = [

    path('login/', auth_views.LoginView.as_view() , name='login'),
    path('logout/', auth_views.LogoutView.as_view(redirect_field_name='home.html'), name='logout'), #система ищет нейки профайл!
    path('create-account/', users_views.EmployeeCreateView.as_view() , name='create-account'),
    path('create/', users_views.UserCreateView.as_view() , name='create'),
    #path('create/', auth_views.CustomerCreateView.as_view()),
    #

]