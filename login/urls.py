from django.contrib import admin
from django.urls import path
from . import views

app_name ="login"
urlpatterns = [
    path('', views.IndexClass.as_view(), name='index'),
]
