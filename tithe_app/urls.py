from django.urls import path
from . import views


app_name = 'tithe_app'

urlpatterns = [

    # path('', views.base, name='base'),
    path('create/', views.create, name='create'),

] 