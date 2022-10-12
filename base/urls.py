from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forum/<str:pk>/', views.forum, name='forum'),                  #<str:pk> add string 'pk' by default to url
    path('user_profile/<str:pk>/', views.user_profile, name='user_profile'),
    path('create_room/', views.create_room, name='create_room'),
    path('update_room/<str:pk>/', views.update_room, name='update_room'),
    path('delete_room/<str:pk>/', views.delete_room, name='delete_room'),
    path('delete_message/<str:pk>', views.delete_message, name='delete_message')
]
