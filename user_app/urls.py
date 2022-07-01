from django.urls import path
from . import views


app_name = 'user_app'

urlpatterns = [

    path('', views.base, name='base'),
    path('login/', views.login, name='login'),
    path('dashboard/<str:username>', views.profile, name = 'profile'),
    path('register/', views.register, name = 'register'),
    path('logout/', views.logout, name = 'logout'),
    path('accounts/dashboard/', views.profile, name = 'profile'),
    path('accounts/login/', views.login, name='login'),
    path('test/', views.test, name='test')

] 