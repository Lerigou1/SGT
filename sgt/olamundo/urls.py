from django.urls import path
from . import views

urlpatterns = [
    #path("", views.index, name="ola"),
    #path("<str:nome>", views.ola, name="oi"),
    path("<str:name>", views.tiadozap, name="oi"),
    #path("<str:nome>", views.saudacao, name="saudacao"),
]
