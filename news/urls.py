from django.urls import path, include
from . import views

app_name = "news"
urlpatterns = [
    path('', views.IndexClass.as_view(),  name='index'),
    # path('add/', views.PostClass.as_view(),  name='add'),
    path('save/', views.SaveClass.as_view(), name='save'),
    path('email/', views.email_view, name='email'),
    path('email_process/', views.email_process, name='email_process'),
]  
 