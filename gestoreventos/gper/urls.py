from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("unidadMedida")
    path("unidadMedida/new", views.UnidadMedidaNew, name="UMnew"),
]