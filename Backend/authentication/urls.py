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
]
