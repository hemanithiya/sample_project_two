from django.contrib import admin
from django.urls import path
from two_app import views
urlpatterns = [
    path('',views.formpage,name='formpage'),
]
