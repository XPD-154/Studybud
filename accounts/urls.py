from django.urls import path
from . import views

urlpatterns = [
    path('', views.accounts, name='accounts'),
    path('login/', views.loginpage, name='loginpage'),
    path('logout/', views.logout, name='logout'),
]
