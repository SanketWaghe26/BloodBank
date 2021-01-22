from django.urls import path
from bloodapp import views

urlpatterns = [
     path('', views.home, name='home'),
     path('contact', views.contact, name='contact'),
     path('about', views.about, name='about'),
     path('donor', views.donor, name='donor'),
     path('search', views.search, name='search')
]

