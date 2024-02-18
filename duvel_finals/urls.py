from django.contrib import admin
from django.urls import path
from . import views

app_name = "duvel_finals"
urlpatterns = [
    path("", views.duvel_finals, name="duvel_finals"),
]
