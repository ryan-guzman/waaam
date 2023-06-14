"""waaam_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from django.views.generic.base import TemplateView # new
from . import views

urlpatterns = [
    path('', views.add_individual_hours, name="add_individual_hours"),
    # path('add_group_hours/', views.add_group_hours, name="add_group_hours"),
    path('dashboard/', views.history, name="history"), #all
    path('export/', views.export, name='export'),
    path('export/', views.export_csv, name='export_csv'),
    path('success/', views.success, name="success"),
    path('profile/', views.profile, name="profile"),
    path('update-profile/', views.update_profile, name="update_profile"),
    path('export_contact/', views.export_contact, name='export_contact'),
    path('add-volunteer/', views.add_volunteer, name='add_volunteer'),
    path('users/', views.json, name='json'),
    path("select2/", include("django_select2.urls")),
    path("signup/", views.signup, name="signup"),
]
