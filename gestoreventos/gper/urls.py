from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("unidadMedida", views.UnidadMedidaList, name="UM"),
    path("unidadMedida/new", views.UnidadMedidaNew, name="UMnew"),
    path("ingrediente", views.IngredienteList, name="Ingrediente"),
    path("ingrediente/new", views.IngredienteNew, name="Ingredientenew"),
]