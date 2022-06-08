from django.urls import path
from . import views


app_name = 'benov_app'

urlpatterns = [

    path('create/', views.create_need, name='create_need'),

] 