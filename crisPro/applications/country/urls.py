from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "Country_app"

urlpatterns = [
        path('NewCountry/',
                views.NewCountry.as_view(),
                name='NewCountry')
]