from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signin', views.signin, name="signin"),
    path('register', views.register, name="register"),
    path('signout', views.signout, name="signout"),
    path("contact", views.contact, name="contact"),
    path("faq", views.faq, name="faq"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path("profile", views.profile, name="profile"),
    path("api", views.api, name="api"),
    path("dashboard", views.dashboard, name="dashboard"),
   
    path("services", views.services, name="services"),
    path("setting", views.setting, name="setting"),
    path("setting1", views.setting1, name="setting1"),
    path("setting2", views.setting2, name="setting2"),
    path("setting3", views.setting3, name="setting3"),
    path("tutorial", views.tutorial, name="tutorial"),


]
