from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path(r'(?P<slug>[\w-]+)/$', views.almost_static, name='pages'),

]