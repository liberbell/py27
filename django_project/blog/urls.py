from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('business', views.business, name='business'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
]