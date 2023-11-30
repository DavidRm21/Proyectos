from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "Language_app"

urlpatterns = [
        path('NewLanguage/',
                views.NewLanguage.as_view(),
                name='NewLanguage')
]