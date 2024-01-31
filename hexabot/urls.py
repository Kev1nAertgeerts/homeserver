from django.contrib import admin
from django.urls import path
from . import views

app_name = "hexabot"
urlpatterns = [
    path("", views.hexabot, name="hexabot"),
]
