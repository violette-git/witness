from django.urls import path
from . import views


app_name = 'benov_app'

urlpatterns = [

    path('', views.base, name='base'),
    path('whereami/', views.whereami, name='whereami'),

    # path('create/', views.create, name='create'),

] 