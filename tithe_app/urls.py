from django.urls import path
from . import views


app_name = 'tithe_app'

urlpatterns = [

    path('needs-list', views.needsbutton, name='needsbutton'),
    path('create/', views.create, name='create'),
    path('contribute/<str:need_id>', views.contribute, name='contribute'),
    path('need-details/<str:need_id>', views.need_details, name='need-details')

] 