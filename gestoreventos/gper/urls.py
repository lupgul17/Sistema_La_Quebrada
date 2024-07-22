from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #unidadMedida
    path('unidadmedida/', views.UnidadMedidaListView.as_view(), name="UnidadMedidaList"),
    path('unidadmedida/<int:pk>/', views.UnidadMedidaDetailView.as_view(), name="UnidadMedidaDetail"),
    path('unidadmedida/new/', views.UnidadMedidaCreateView.as_view(), name="UnidadMedidaNew"), 
    path('unidadmedida/<int:pk>/edit/', views.UnidadMedidaUpdateView.as_view(), name= "UnidadMedidaEdit"),
    path('unidadmedida/<int:pk>/delete/', views.UnidadMedidaDeleteView.as_view(), name="UnidadMedidaDelete"),
    #Ingrediente
    path('ingrediente/', views.IngredienteListView.as_view(), name="IngredienteList"),
    path('ingrediente/<int:pk>/', views.IngredienteDetailView.as_view(), name="IngredienteDetail"),
    path('ingrediente/new/', views.IngredienteCreateView.as_view(), name="IngredienteNew"), 
    path('ingrediente/<int:pk>/edit/', views.IngredienteUpdateView.as_view(), name= "IngredienteEdit"),
    path('ingrediente/<int:pk>/delete/', views.IngredienteDeleteView.as_view(), name="IngredienteDelete"),
    #TecnicaCoccion
    path('tecnicacoccion/', views.TecnicaCoccionListView.as_view(), name="TecnicaCoccionList"),
    path('tecnicacoccion/<int:pk>/', views.TecnicaCoccionDetailView.as_view(), name="TecnicaCoccionDetail"),
    path('tecnicacoccion/new/', views.TecnicaCoccionCreateView.as_view(), name="TecnicaCoccionNew"), 
    path('tecnicacoccion/<int:pk>/edit/', views.TecnicaCoccionUpdateView.as_view(), name= "TecnicaCoccionEdit"),
    path('tecnicacoccion/<int:pk>/delete/', views.TecnicaCoccionDeleteView.as_view(), name="TecnicaCoccionDelete"),
    #Origen
    path('origen/', views.OrigenListView.as_view(), name="OrigenList"),
    path('origen/<int:pk>/', views.OrigenDetailView.as_view(), name="OrigenDetail"),
    path('origen/new/', views.OrigenCreateView.as_view(), name="OrigenNew"), 
    path('origen/<int:pk>/edit/', views.OrigenUpdateView.as_view(), name= "OrigenEdit"),
    path('origen/<int:pk>/delete/', views.OrigenDeleteView.as_view(), name="OrigenDelete"),
    #Menu
    path('menu/', views.MenuListView.as_view(), name="MenuList"),
    path('menu/<int:pk>/', views.MenuDetailView.as_view(), name="MenuDetail"),
    path('menu/new/', views.MenuCreateView.as_view(), name="MenuNew"), 
    path('menu/<int:pk>/edit/', views.MenuUpdateView.as_view(), name= "MenuEdit"),
    path('menu/<int:pk>/delete/', views.MenuDeleteView.as_view(), name="MenuDelete"),
    #Receta
    path('receta/', views.RecetaListView.as_view(), name="RecetaList"),
    path('receta/<int:pk>/', views.RecetaDetailView.as_view(), name="RecetaDetail"),
    path('receta/new/', views.RecetaCreateView.as_view(), name="RecetaNew"), 
    path('receta/<int:pk>/edit/', views.RecetaUpdateView.as_view(), name= "RecetaEdit"),
    path('receta/<int:pk>/delete/', views.RecetaDeleteView.as_view(), name="RecetaDelete"),
    #TecnicasReceta
    path('tecnicasreceta/', views.TecnicasRecetaListView.as_view(), name="TecnicasRecetaList"),
    path('tecnicasreceta/<int:pk>/', views.TecnicasRecetaDetailView.as_view(), name="TecnicasRecetaDetail"),
    path('tecnicasreceta/new/', views.TecnicasRecetaCreateView.as_view(), name="TecnicasRecetaNew"), 
    path('tecnicasreceta/<int:pk>/edit/', views.TecnicasRecetaUpdateView.as_view(), name= "TecnicasRecetaEdit"),
    path('tecnicasreceta/<int:pk>/delete/', views.TecnicasRecetaDeleteView.as_view(), name="TecnicasRecetaDelete"),
    #IngredientesReceta
    path('ingredientesreceta/', views.IngredientesRecetaListView.as_view(), name="IngredientesRecetaList"),
    path('ingredientesreceta/<int:pk>/', views.IngredientesRecetaDetailView.as_view(), name="IngredientesRecetaDetail"),
    path('ingredientesreceta/new/', views.IngredientesRecetaCreateView.as_view(), name="IngredientesRecetaNew"), 
    path('ingredientesreceta/<int:pk>/edit/', views.IngredientesRecetaUpdateView.as_view(), name= "IngredientesRecetaEdit"),
    path('ingredientesreceta/<int:pk>/delete/', views.IngredientesRecetaDeleteView.as_view(), name="IngredientesRecetaDelete"),
    #RecetaCostos
    path('recetacostos/', views.RecetaCostosListView.as_view(), name="RecetaCostosList"),
    path('recetacostos/<int:pk>/', views.RecetaCostosDetailView.as_view(), name="RecetaCostosDetail"),
    path('recetacostos/new/', views.RecetaCostosCreateView.as_view(), name="RecetaCostosNew"), 
    path('recetacostos/<int:pk>/edit/', views.RecetaCostosUpdateView.as_view(), name= "RecetaCostosEdit"),
    path('recetacostos/<int:pk>/delete/', views.RecetaCostosDeleteView.as_view(), name="RecetaCostosDelete"),
    #MenuRecetas
    path('menurecetas/', views.MenuRecetasListView.as_view(), name="MenuRecetasList"),
    path('menurecetas/<int:pk>/', views.MenuRecetasDetailView.as_view(), name="MenuRecetasDetail"),
    path('menurecetas/new/', views.MenuRecetasCreateView.as_view(), name="MenuRecetasNew"), 
    path('menurecetas/<int:pk>/edit/', views.MenuRecetasUpdateView.as_view(), name= "MenuRecetasEdit"),
    path('menurecetas/<int:pk>/delete/', views.MenuRecetasDeleteView.as_view(), name="MenuRecetasDelete"),
    #Clientes
    path('cliente/', views.ClienteListView.as_view(), name="ClienteList"),
    path('cliente/<int:pk>/', views.ClienteDetailView.as_view(), name="ClienteDetail"),
    path('cliente/new/', views.ClienteCreateView.as_view(), name="ClienteNew"), 
    path('cliente/<int:pk>/edit/', views.ClienteUpdateView.as_view(), name= "ClienteEdit"),
    path('cliente/<int:pk>/delete/', views.ClienteDeleteView.as_view(), name="ClienteDelete"),
    #ServiciosOpcionales
    path('serviciosopcionales/', views.ServiciosOpcionalesListView.as_view(), name="ServiciosOpcionalesList"),
    path('serviciosopcionales/<int:pk>/', views.ServiciosOpcionalesDetailView.as_view(), name="ServiciosOpcionalesDetail"),
    path('serviciosopcionales/new/', views.ServiciosOpcionalesCreateView.as_view(), name="ServiciosOpcionalesNew"), 
    path('serviciosopcionales/<int:pk>/edit/', views.ServiciosOpcionalesUpdateView.as_view(), name= "ServiciosOpcionalesEdit"),
    path('serviciosopcionales/<int:pk>/delete/', views.ServiciosOpcionalesDeleteView.as_view(), name="ServiciosOpcionalesDelete"),
    #Lugar
    path('lugar/', views.LugarListView.as_view(), name="LugarList"),
    path('lugar/<int:pk>/', views.LugarDetailView.as_view(), name="LugarDetail"),
    path('lugar/new/', views.LugarCreateView.as_view(), name="LugarNew"), 
    path('lugar/<int:pk>/edit/', views.LugarUpdateView.as_view(), name= "LugarEdit"),
    path('lugar/<int:pk>/delete/', views.LugarDeleteView.as_view(), name="LugarDelete"),
    #Evento
    path('evento/', views.EventoListView.as_view(), name="EventoList"),
    path('evento/<int:pk>/', views.EventoDetailView.as_view(), name="EventoDetail"),
    path('evento/new/', views.EventoCreateView.as_view(), name="EventoNew"), 
    path('evento/<int:pk>/edit/', views.EventoUpdateView.as_view(), name= "EventoEdit"),
    path('evento/<int:pk>/delete/', views.EventoDeleteView.as_view(), name="EventoDelete"),
    #ServiciosOpcionalesLista
    path('serviciosopcionaleslista/', views.ServiciosOpcionalesListaListView.as_view(), name="ServiciosOpcionalesListaList"),
    path('serviciosopcionaleslista/<int:pk>/', views.ServiciosOpcionalesListaDetailView.as_view(), name="ServiciosOpcionalesListaDetail"),
    path('serviciosopcionaleslista/new/', views.ServiciosOpcionalesListaCreateView.as_view(), name="ServiciosOpcionalesListaNew"), 
    path('serviciosopcionaleslista/<int:pk>/edit/', views.ServiciosOpcionalesListaUpdateView.as_view(), name= "ServiciosOpcionalesListaEdit"),
    path('serviciosopcionaleslista/<int:pk>/delete/', views.ServiciosOpcionalesListaDeleteView.as_view(), name="ServiciosOpcionalesListaDelete"),
    #ListadoMenus
    path('listadomenus/', views.ListadoMenusListView.as_view(), name="ListadoMenusList"),
    path('listadomenus/<int:pk>/', views.ListadoMenusDetailView.as_view(), name="ListadoMenusDetail"),
    path('listadomenus/new/', views.ListadoMenusCreateView.as_view(), name="ListadoMenusNew"), 
    path('listadomenus/<int:pk>/edit/', views.ListadoMenusUpdateView.as_view(), name= "ListadoMenusEdit"),
    path('listadomenus/<int:pk>/delete/', views.ListadoMenusDeleteView.as_view(), name="ListadoMenusDelete"),
]