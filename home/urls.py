from django.urls import path
from . import views

urlpatterns = [
    path('', views.comingsoon, name='comingsoon'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('comm/', views.comm, name='comm'),
    path('comm/addcomment/', views.addcomment, name='addcomment'),
]