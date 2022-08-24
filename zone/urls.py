from django.contrib import admin
from django.urls import path
from zone import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('form/', views.form),

]
