
from django.urls import path
from . import views

app_name = 'bank'
urlpatterns = [
    path('', views.index, name='index'),
    path('single-page/', views.single, name='single'),
]