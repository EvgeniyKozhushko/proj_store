from django.urls import path

from comments import views as comments_views

app_name = 'comments'

urlpatterns = [

    path('create-comment', comments_views.CommentCreateView.as_view(), name='create-comment'),

]