"""
Definition of urls for WORKPROJECT.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.http import HttpResponse

def home(request):
    return HttpResponse('Home Page')


urlpatterns = [
    path('', views.home, name='home'),
    path('casestudy/', views.casestudy, name='casestudy'),
    path('contact/', views.contact, name='contact'),
    path('consultation/',views.consultation, name='consultation'),
    path('clients/', views.clients, name='clients'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('marketing/', views.marketing, name='marketing'),
    path('',home),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
