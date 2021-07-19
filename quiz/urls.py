from django.contrib import admin
from django.urls import path
from quiz import views

app_name = "base"

urlpatterns = [
    path("",views.index,name='index'),
    path("check/",views.check,name='check')
]

