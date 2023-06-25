from django.contrib import admin
from django.urls import path,include
from law import views

admin.site.site_header = "Better Call Saul Employee Login"
admin.site.index_title = "Welcome"



urlpatterns = [
    path('', views.index,name='home'),
    path('rights', views.rights,name='rights'),
    path('contact', views.contact,name='contact'),
    path('about', views.about,name='about'),
]
