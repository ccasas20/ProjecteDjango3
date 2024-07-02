from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("preguntes/", views.preguntes, name="preguntes"),
    path("resultats/", views.resultats, name="resultats"),
]
