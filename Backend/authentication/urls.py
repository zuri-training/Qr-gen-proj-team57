from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signin', views.signin, name="signin"),
    path('register', views.register, name="register"),
    path('signout', views.signout, name="signout"),
]
