from django.urls import path
from . import views


app_name = 'org_app'

urlpatterns = [

    path('register-org', views.create_org, name='create-org'),
    path('orgs/', views.orgs, name='orgs'),

] 