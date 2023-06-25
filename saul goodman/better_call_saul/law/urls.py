from django.contrib import admin
from django.urls import path
from law import views

urlpatterns = [
    path('', views.index,name='home'),
    path('rights', views.rights,name='rights'),
    path('contact', views.contact,name='contact'),
    path('about', views.about,name='about'),
]
