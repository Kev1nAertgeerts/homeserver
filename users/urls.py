from django.contrib import admin
from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("login/", views.login_page, name="login"),
    path('logout/', views.sign_out, name='logout'),
]
