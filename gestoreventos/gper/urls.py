from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('unidadmedida/', views.UnidadMedidaListView.as_view(), name="UnidadMedidaList"),
    path('unidadmedida/<int:pk>/', views.UnidadMedidaDetailView.as_view(), name="UnidadMedidaDetail"),
    path('unidadmedida/new/', views.UnidadMedidaCreateView.as_view(), name="UnidadMedidaNew"), 
    path('unidadmedida/<int:pk>/edit/', views.UnidadMedidaUpdateView.as_view(), name= "UnidadMedidaEdit"),
    path('unidadmedida/<int:pk>/delete/', views.UnidadMedidaDeleteView.as_view(), name="UnidadMedidaDelete"),
    
]