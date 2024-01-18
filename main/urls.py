from django.contrib import admin
from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("home/", views.home_page, name="home"),
    path("digitale-meter/", views.digi_meter_page, name="digi-meter"),
    path("it-tegenw-tijd/", views.tegenw_tijd_page, name="tegenw-tijd"),
    path("diepvries/", views.diepvries_page, name="diepvries"),
]
