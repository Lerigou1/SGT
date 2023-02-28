from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ola"),
    path("<str:nome>", views.saudacao, name="saudacao")
]
