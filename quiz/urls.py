from django.contrib import admin
from django.urls import path
from quiz import views

app_name = "base"

urlpatterns = [
    path("python/",views.python,name='python'),
    path("check/",views.check,name='check'),
    path("", views.index, name='index'),
    path("score/",views.score),
    path("myaccount/",views.myaccount,name="myaccount"),
    path("login/",views.login,name="login"),
    path("signup/",views.signup,name='signup'),
    path("verify/",views.verify,name='verify'),
    path("account/",views.account,name='account'),
    path("logout/",views.logout,name='logout'),
    path("cplus/",views.cplus,name='cplus'),
    path("cquiz/", views.cquiz, name='cquiz'),
    path("c/",views.ccheck,name='c'),
    path("cprog/",views.c, name='cprog'),
    path("short/",views.short, name='short')

]


