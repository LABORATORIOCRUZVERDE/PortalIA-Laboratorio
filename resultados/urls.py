from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_resultados, name="lista_resultados"),
]