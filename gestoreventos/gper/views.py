from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return HttpResponse("Hola Mundo xD")

#region CRUD UnidadMedida
class UnidadMedidaListView(ListView):
    model = UnidadMedida
    template_name = 'Unidades.html'

class UnidadMedidaDetailView(DetailView):
    model = UnidadMedida
    template_name = "UnidadesDetalle.html"

class UnidadMedidaCreateView(CreateView):
    model = UnidadMedida
    form_class = UnidadMedidaForm
    template_name = 'UnidadForm.html'
    success_url = reverse_lazy("UnidadMedidaList")

class UnidadMedidaUpdateView(UpdateView):
    model = UnidadMedida
    form_class = UnidadMedidaForm
    template_name = 'UnidadForm.html'
    success_url = reverse_lazy("UnidadMedidaList")

class UnidadMedidaDeleteView(DeleteView):
    model = UnidadMedida
    template_name = 'UnidadDeleteForm.html'
    success_url = reverse_lazy("UnidadMedidaList")

#endregion

#region CRUD Ingrediente
class IngredienteListView(ListView):
    model = Ingrediente
    template_name = 'Ingredientes.html'

class IngredienteDetailView(DetailView):
    model = Ingrediente
    template_name = "IngredientesDetalle.html"

class IngredienteCreateView(CreateView):
    model = Ingrediente
    form_class = IngredienteForm
    template_name = 'IngredienteForm.html'
    success_url = reverse_lazy("IngredienteList")

class IngredienteUpdateView(UpdateView):
    model = Ingrediente
    form_class = IngredienteForm
    template_name = 'IngredienteForm.html'
    success_url = reverse_lazy("IngredienteList")

class IngredienteDeleteView(DeleteView):
    model = Ingrediente
    template_name = 'IngredienteDeleteForm.html'
    success_url = reverse_lazy("IngredienteList")
#endregion
#region CRUD TecnicaCoccion
class TecnicaCoccionListView(ListView):
    model = TecnicaCoccion
    template_name = 'TecnicasCoccion.html'

class TecnicaCoccionDetailView(DetailView):
    model = TecnicaCoccion
    template_name = "TecnicasCoccionDetalle.html"

class TecnicaCoccionCreateView(CreateView):
    model = TecnicaCoccion
    form_class = TecnicaCoccionForm
    template_name = 'TecnicaCoccionForm.html'
    success_url = reverse_lazy("TecnicaCoccionList")

class TecnicaCoccionUpdateView(UpdateView):
    model = TecnicaCoccion
    form_class = TecnicaCoccionForm
    template_name = 'TecnicaCoccionForm.html'
    success_url = reverse_lazy("TecnicaCoccionList")

class TecnicaCoccionDeleteView(DeleteView):
    model = TecnicaCoccion
    template_name = 'TecnicaCoccionDeleteForm.html'
    success_url = reverse_lazy("TecnicaCoccionList")
#endregion

#region CRUD Origen
class OrigenListView(ListView):
    model = Origen
    template_name = 'Origenes.html'

class OrigenDetailView(DetailView):
    model = Origen
    template_name = "OrigenDetalle.html"

class OrigenCreateView(CreateView):
    model = Origen
    form_class = OrigenForm
    template_name = 'OrigenForm.html'
    success_url = reverse_lazy("OrigenList")

class OrigenUpdateView(UpdateView):
    model = Origen
    form_class = OrigenForm
    template_name = 'OrigenForm.html'
    success_url = reverse_lazy("OrigenList")

class OrigenDeleteView(DeleteView):
    model = Origen
    template_name = 'OrigenDeleteForm.html'
    success_url = reverse_lazy("OrigenList")

#endregion
#region CRUD Menu

class MenuListView(ListView):
    model = Menu
    template_name = 'Menus.html'

class MenuDetailView(DetailView):
    model = Menu
    template_name = "MenuDetalle.html"

class MenuCreateView(CreateView):
    model = Menu
    form_class = MenuForm
    template_name = 'MenuForm.html'
    success_url = reverse_lazy("MenuList")

class MenuUpdateView(UpdateView):
    model = Menu
    form_class = MenuForm
    template_name = 'MenuForm.html'
    success_url = reverse_lazy("MenuList")

class MenuDeleteView(DeleteView):
    model = Menu
    template_name = 'MenuDeleteForm.html'
    success_url = reverse_lazy("MenuList")
#endregion

#region CRUD Receta
class RecetaListView(ListView):
    model = Receta
    template_name = 'Recetas.html'

class RecetaDetailView(DetailView):
    model = Receta
    template_name = "RecetaDetalle.html"

class RecetaCreateView(CreateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'RecetaForm.html'
    success_url = reverse_lazy("RecetaList")

class RecetaUpdateView(UpdateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'RecetaForm.html'
    success_url = reverse_lazy("RecetaList")

class RecetaDeleteView(DeleteView):
    model = Receta
    template_name = 'RecetaDeleteForm.html'
    success_url = reverse_lazy("RecetaList")
#endregion
#region CRUD TecnicasReceta
class TecnicasRecetaListView(ListView):
    model = TecnicasReceta
    template_name = 'TecnicasRecetas.html'

class TecnicasRecetaDetailView(DetailView):
    model = TecnicasReceta
    template_name = "TecnicasRecetaDetalle.html"

class TecnicasRecetaCreateView(CreateView):
    model = TecnicasReceta
    form_class = TecnicasRecetaForm
    template_name = 'TecnicasRecetaForm.html'
    success_url = reverse_lazy("TecnicasRecetaList")

class TecnicasRecetaUpdateView(UpdateView):
    model = TecnicasReceta
    form_class = TecnicasRecetaForm
    template_name = 'TecnicasRecetaForm.html'
    success_url = reverse_lazy("TecnicasRecetaList")

class TecnicasRecetaDeleteView(DeleteView):
    model = TecnicasReceta
    template_name = 'TecnicasRecetaDeleteForm.html'
    success_url = reverse_lazy("TecnicasRecetaList")
#endregion
#region CRUD IngredientesReceta
class IngredientesRecetaListView(ListView):
    model = IngredientesReceta
    template_name = 'IngredientesRecetas.html'

class IngredientesRecetaDetailView(DetailView):
    model = IngredientesReceta
    template_name = "IngredientesRecetaDetalle.html"

class IngredientesRecetaCreateView(CreateView):
    model = IngredientesReceta
    form_class = IngredientesRecetaForm
    template_name = 'IngredientesRecetaForm.html'
    success_url = reverse_lazy("IngredientesRecetaList")

class IngredientesRecetaUpdateView(UpdateView):
    model = IngredientesReceta
    form_class = IngredientesRecetaForm
    template_name = 'IngredientesRecetaForm.html'
    success_url = reverse_lazy("IngredientesRecetaList")

class IngredientesRecetaDeleteView(DeleteView):
    model = IngredientesReceta
    template_name = 'IngredientesRecetaDeleteForm.html'
    success_url = reverse_lazy("IngredientesRecetaList")
#endregion

#region CRUD RecetaCostos
class RecetaCostosListView(ListView):
    model = RecetaCostos
    template_name = 'RecetaCostos.html'

class RecetaCostosDetailView(DetailView):
    model = RecetaCostos
    template_name = "RecetaCostosDetalle.html"

class RecetaCostosCreateView(CreateView):
    model = RecetaCostos
    form_class = RecetaCostosForm
    template_name = 'RecetaCostosForm.html'
    success_url = reverse_lazy("RecetaCostosList")

class RecetaCostosUpdateView(UpdateView):
    model = RecetaCostos
    form_class = RecetaCostosForm
    template_name = 'RecetaCostosForm.html'
    success_url = reverse_lazy("RecetaCostosList")

class RecetaCostosDeleteView(DeleteView):
    model = RecetaCostos
    template_name = 'RecetaCostosDeleteForm.html'
    success_url = reverse_lazy("RecetaCostosList")
#endregion

#region CRUD MenuRecetas
class MenuRecetasListView(ListView):
    model = MenuRecetas
    template_name = 'MenuRecetas.html'

class MenuRecetasDetailView(DetailView):
    model = MenuRecetas
    template_name = "MenuRecetasDetalle.html"

class MenuRecetasCreateView(CreateView):
    model = MenuRecetas
    form_class = MenuRecetasForm
    template_name = 'MenuRecetasForm.html'
    success_url = reverse_lazy("MenuRecetasList")

class MenuRecetasUpdateView(UpdateView):
    model = MenuRecetas
    form_class = MenuRecetasForm
    template_name = 'MenuRecetasForm.html'
    success_url = reverse_lazy("MenuRecetasList")

class MenuRecetasDeleteView(DeleteView):
    model = MenuRecetas
    template_name = 'MenuRecetasDeleteForm.html'
    success_url = reverse_lazy("MenuRecetasList")
#endregion

#region CRUD Cliente
class ClienteListView(ListView):
    model = Cliente
    template_name = 'Clientes.html'

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "ClienteDetalle.html"

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'ClienteForm.html'
    success_url = reverse_lazy("ClienteList")

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'ClienteForm.html'
    success_url = reverse_lazy("ClienteList")

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'ClienteDeleteForm.html'
    success_url = reverse_lazy("ClienteList")
#endregion

#region CRUD ServiciosOpcionales
class ServiciosOpcionalesListView(ListView):
    model = ServiciosOpcionales
    template_name = 'ServiciosOpcionales.html'

class ServiciosOpcionalesDetailView(DetailView):
    model = ServiciosOpcionales
    template_name = "ServiciosOpcionalesDetalle.html"

class ServiciosOpcionalesCreateView(CreateView):
    model = ServiciosOpcionales
    form_class = ServiciosOpcionalesForm
    template_name = 'ServiciosOpcionalesForm.html'
    success_url = reverse_lazy("ServiciosOpcionalesList")

class ServiciosOpcionalesUpdateView(UpdateView):
    model = ServiciosOpcionales
    form_class = ServiciosOpcionalesForm
    template_name = 'ServiciosOpcionalesForm.html'
    success_url = reverse_lazy("ServiciosOpcionalesList")

class ServiciosOpcionalesDeleteView(DeleteView):
    model = ServiciosOpcionales
    template_name = 'ServiciosOpcionalesDeleteForm.html'
    success_url = reverse_lazy("ServiciosOpcionalesList")
#endregion

#region CRUD Lugar
class LugarListView(ListView):
    model = Lugar
    template_name = 'Lugares.html'

class LugarDetailView(DetailView):
    model = Lugar
    template_name = "LugarDetalle.html"

class LugarCreateView(CreateView):
    model = Lugar
    form_class = LugarForm
    template_name = 'LugarForm.html'
    success_url = reverse_lazy("LugarList")

class LugarUpdateView(UpdateView):
    model = Lugar
    form_class = LugarForm
    template_name = 'LugarForm.html'
    success_url = reverse_lazy("LugarList")

class LugarDeleteView(DeleteView):
    model = Lugar
    template_name = 'LugarDeleteForm.html'
    success_url = reverse_lazy("LugarList")
#endregion

#region CRUD Evento
class EventoListView(ListView):
    model = Evento
    template_name = 'Eventos.html'

class EventoDetailView(DetailView):
    model = Evento
    template_name = "EventoDetalle.html"

class EventoCreateView(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'EventoForm.html'
    success_url = reverse_lazy("EventoList")

class EventoUpdateView(UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'EventoForm.html'
    success_url = reverse_lazy("EventoList")

class EventoDeleteView(DeleteView):
    model = Evento
    template_name = 'EventoDeleteForm.html'
    success_url = reverse_lazy("EventoList")

#endregion

#region CRUD ServiciosOpcionalesLista
class ServiciosOpcionalesListaListView(ListView):
    model = ServiciosOpcionalesLista
    template_name = 'ServiciosOpcionalesListas.html'

class ServiciosOpcionalesListaDetailView(DetailView):
    model = ServiciosOpcionalesLista
    template_name = "ServiciosOpcionalesListaDetalle.html"

class ServiciosOpcionalesListaCreateView(CreateView):
    model = ServiciosOpcionalesLista
    form_class = ServiciosOpcionalesListaForm
    template_name = 'ServiciosOpcionalesListaForm.html'
    success_url = reverse_lazy("ServiciosOpcionalesListaList")

class ServiciosOpcionalesListaUpdateView(UpdateView):
    model = ServiciosOpcionalesLista
    form_class = ServiciosOpcionalesListaForm
    template_name = 'ServiciosOpcionalesListaForm.html'
    success_url = reverse_lazy("ServiciosOpcionalesListaList")

class ServiciosOpcionalesListaDeleteView(DeleteView):
    model = ServiciosOpcionalesLista
    template_name = 'ServiciosOpcionalesListaDeleteForm.html'
    success_url = reverse_lazy("ServiciosOpcionalesListaList")
#endregion

#region CRUD ListadoMenus
class ListadoMenusListView(ListView):
    model = ListadoMenus
    template_name = 'ListadoMenus.html'

class ListadoMenusDetailView(DetailView):
    model = ListadoMenus
    template_name = "ListadoMenusDetalle.html"

class ListadoMenusCreateView(CreateView):
    model = ListadoMenus
    form_class = ListadoMenusForm
    template_name = 'ListadoMenusForm.html'
    success_url = reverse_lazy("ListadoMenusList")

class ListadoMenusUpdateView(UpdateView):
    model = ListadoMenus
    form_class = ListadoMenusForm
    template_name = 'ListadoMenusForm.html'
    success_url = reverse_lazy("ListadoMenusList")

class ListadoMenusDeleteView(DeleteView):
    model = ListadoMenus
    template_name = 'ListadoMenusDeleteForm.html'
    success_url = reverse_lazy("ListadoMenusList")
#endregion

