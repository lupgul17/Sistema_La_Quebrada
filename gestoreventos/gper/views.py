from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import *
from .forms import *
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    return render(request, 'main.html')

#region CRUD UnidadMedida
class UnidadMedidaListView(LoginRequiredMixin, ListView):
    model = UnidadMedida
    template_name = 'UnidadMedida/Unidades.html'


class UnidadMedidaDetailView(LoginRequiredMixin, DetailView):
    model = UnidadMedida
    template_name = "UnidadMedida/UnidadesDetalle.html"

class UnidadMedidaCreateView(LoginRequiredMixin, CreateView):
    model = UnidadMedida
    form_class = UnidadMedidaForm
    template_name = 'UnidadMedida/UnidadForm.html'
    success_url = reverse_lazy("UnidadMedidaList")

class UnidadMedidaUpdateView(LoginRequiredMixin, UpdateView):
    model = UnidadMedida
    form_class = UnidadMedidaForm
    template_name = 'UnidadMedida/UnidadForm.html'
    success_url = reverse_lazy("UnidadMedidaList")

class UnidadMedidaDeleteView(LoginRequiredMixin, DeleteView):
    model = UnidadMedida
    template_name = 'UnidadMedida/UnidadDeleteForm.html'
    success_url = reverse_lazy("UnidadMedidaList")

#endregion

#region CRUD Ingrediente
class IngredienteListView(LoginRequiredMixin, ListView):
    model = Ingrediente
    template_name = 'Ingredientes/Ingredientes.html'

class IngredienteDetailView(LoginRequiredMixin, DetailView):
    model = Ingrediente
    template_name = "Ingredientes/IngredientesDetalle.html"

class IngredienteCreateView(LoginRequiredMixin, CreateView):
    model = Ingrediente
    form_class = IngredienteForm
    template_name = 'Ingredientes/IngredienteForm.html'
    success_url = reverse_lazy("IngredienteList")

class IngredienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingrediente
    form_class = IngredienteForm
    template_name = 'Ingredientes/IngredienteForm.html'
    success_url = reverse_lazy("IngredienteList")

class IngredienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingrediente
    template_name = 'Ingredientes/IngredienteDeleteForm.html'
    success_url = reverse_lazy("IngredienteList")
#endregion
#region CRUD TecnicaCoccion
class TecnicaCoccionListView(ListView):
    model = TecnicaCoccion
    template_name = 'TecnicaCoccion/TecnicasCoccion.html'

class TecnicaCoccionDetailView(DetailView):
    model = TecnicaCoccion
    template_name = "TecnicaCoccion/TecnicasCoccionDetalle.html"

class TecnicaCoccionCreateView(CreateView):
    model = TecnicaCoccion
    form_class = TecnicaCoccionForm
    template_name = 'TecnicaCoccion/TecnicaCoccionForm.html'
    success_url = reverse_lazy("TecnicaCoccionList")

class TecnicaCoccionUpdateView(UpdateView):
    model = TecnicaCoccion
    form_class = TecnicaCoccionForm
    template_name = 'TecnicaCoccion/TecnicaCoccionForm.html'
    success_url = reverse_lazy("TecnicaCoccionList")

class TecnicaCoccionDeleteView(DeleteView):
    model = TecnicaCoccion
    template_name = 'TecnicaCoccion/TecnicaCoccionDeleteForm.html'
    success_url = reverse_lazy("TecnicaCoccionList")
#endregion

#region CRUD Origen
class OrigenListView(ListView):
    model = Origen
    template_name = 'Origen/Origenes.html'

class OrigenDetailView(DetailView):
    model = Origen
    template_name = "Origen/OrigenDetalle.html"

class OrigenCreateView(CreateView):
    model = Origen
    form_class = OrigenForm
    template_name = 'Origen/OrigenForm.html'
    success_url = reverse_lazy("OrigenList")

class OrigenUpdateView(UpdateView):
    model = Origen
    form_class = OrigenForm
    template_name = 'Origen/OrigenForm.html'
    success_url = reverse_lazy("OrigenList")

class OrigenDeleteView(DeleteView):
    model = Origen
    template_name = 'Origen/OrigenDeleteForm.html'
    success_url = reverse_lazy("OrigenList")

#endregion
#region CRUD Menu

class MenuListView(ListView):
    model = Menu
    template_name = 'Menu/Menus.html'

class MenuDetailView(DetailView):
    model = Menu
    template_name = "Menu/MenuDetalle.html"

class MenuCreateView(CreateView):
    model = Menu
    form_class = MenuForm
    template_name = 'Menu/MenuForm.html'
    success_url = reverse_lazy("MenuList")

class MenuUpdateView(UpdateView):
    model = Menu
    form_class = MenuForm
    template_name = 'Menu/MenuForm.html'
    success_url = reverse_lazy("MenuList")

class MenuDeleteView(DeleteView):
    model = Menu
    template_name = 'Menu/MenuDeleteForm.html'
    success_url = reverse_lazy("MenuList")
#endregion

#region CRUD Receta
class RecetaListView(ListView):
    model = Receta
    template_name = 'Receta/Recetas.html'

class RecetaDetailView(DetailView):
    model = Receta
    template_name = "Receta/RecetaDetalle.html"

class RecetaCreateView(CreateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'Receta/RecetaForm.html'
    success_url = reverse_lazy("RecetaList")

class RecetaUpdateView(UpdateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'Receta/RecetaForm.html'
    success_url = reverse_lazy("RecetaList")

class RecetaDeleteView(DeleteView):
    model = Receta
    template_name = 'Receta/RecetaDeleteForm.html'
    success_url = reverse_lazy("RecetaList")
#endregion
#region CRUD TecnicasReceta
class TecnicasRecetaListView(ListView):
    model = TecnicasReceta
    template_name = 'TecnicasReceta/TecnicasRecetas.html'

class TecnicasRecetaDetailView(DetailView):
    model = TecnicasReceta
    template_name = "TecnicasReceta/TecnicasRecetaDetalle.html"

class TecnicasRecetaCreateView(CreateView):
    model = TecnicasReceta
    form_class = TecnicasRecetaForm
    template_name = 'TecnicasReceta/TecnicasRecetaForm.html'
    success_url = reverse_lazy("TecnicasRecetaList")

class TecnicasRecetaUpdateView(UpdateView):
    model = TecnicasReceta
    form_class = TecnicasRecetaForm
    template_name = 'TecnicasReceta/TecnicasRecetaForm.html'
    success_url = reverse_lazy("TecnicasRecetaList")

class TecnicasRecetaDeleteView(DeleteView):
    model = TecnicasReceta
    template_name = 'TecnicasReceta/TecnicasRecetaDeleteForm.html'
    success_url = reverse_lazy("TecnicasRecetaList")
#endregion
#region CRUD IngredientesReceta
class IngredientesRecetaListView(ListView):
    model = IngredientesReceta
    template_name = 'IngredientesReceta/IngredientesRecetas.html'

class IngredientesRecetaDetailView(DetailView):
    model = IngredientesReceta
    template_name = "IngredientesReceta/IngredientesRecetaDetalle.html"

class IngredientesRecetaCreateView(CreateView):
    model = IngredientesReceta
    form_class = IngredientesRecetaForm
    template_name = 'IngredientesReceta/IngredientesRecetaForm.html'
    success_url = reverse_lazy("IngredientesRecetaList")

class IngredientesRecetaUpdateView(UpdateView):
    model = IngredientesReceta
    form_class = IngredientesRecetaForm
    template_name = 'IngredientesReceta/IngredientesRecetaForm.html'
    success_url = reverse_lazy("IngredientesRecetaList")

class IngredientesRecetaDeleteView(DeleteView):
    model = IngredientesReceta
    template_name = 'IngredientesReceta/IngredientesRecetaDeleteForm.html'
    success_url = reverse_lazy("IngredientesRecetaList")
#endregion

#region CRUD RecetaCostos
class RecetaCostosListView(ListView):
    model = RecetaCostos
    template_name = 'RecetaCostos/RecetaCostos.html'

class RecetaCostosDetailView(DetailView):
    model = RecetaCostos
    template_name = "RecetaCostos/RecetaCostosDetalle.html"

class RecetaCostosCreateView(CreateView):
    model = RecetaCostos
    form_class = RecetaCostosForm
    template_name = 'RecetaCostos/RecetaCostosForm.html'
    success_url = reverse_lazy("RecetaCostosList")

class RecetaCostosUpdateView(UpdateView):
    model = RecetaCostos
    form_class = RecetaCostosForm
    template_name = 'RecetaCostos/RecetaCostosForm.html'
    success_url = reverse_lazy("RecetaCostosList")

class RecetaCostosDeleteView(DeleteView):
    model = RecetaCostos
    template_name = 'RecetaCostos/RecetaCostosDeleteForm.html'
    success_url = reverse_lazy("RecetaCostosList")
#endregion

#region CRUD MenuRecetas
class MenuRecetasListView(ListView):
    model = MenuRecetas
    template_name = 'MenuRecetas/MenuRecetas.html'

class MenuRecetasDetailView(DetailView):
    model = MenuRecetas
    template_name = "MenuRecetas/MenuRecetasDetalle.html"

class MenuRecetasCreateView(CreateView):
    model = MenuRecetas
    form_class = MenuRecetasForm
    template_name = 'MenuRecetas/MenuRecetasForm.html'
    success_url = reverse_lazy("MenuRecetasList")

class MenuRecetasUpdateView(UpdateView):
    model = MenuRecetas
    form_class = MenuRecetasForm
    template_name = 'MenuRecetas/MenuRecetasForm.html'
    success_url = reverse_lazy("MenuRecetasList")

class MenuRecetasDeleteView(DeleteView):
    model = MenuRecetas
    template_name = 'MenuRecetas/MenuRecetasDeleteForm.html'
    success_url = reverse_lazy("MenuRecetasList")
#endregion

#region CRUD Cliente
class ClienteListView(ListView):
    model = Cliente
    template_name = 'Cliente/Clientes.html'

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "Cliente/ClienteDetalle.html"

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'Cliente/ClienteForm.html'
    success_url = reverse_lazy("ClienteList")

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'Cliente/ClienteForm.html'
    success_url = reverse_lazy("ClienteList")

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'Cliente/ClienteDeleteForm.html'
    success_url = reverse_lazy("ClienteList")
#endregion

#region CRUD ServiciosOpcionales
class ServiciosOpcionalesListView(ListView):
    model = ServiciosOpcionales
    template_name = 'ServiciosOpcionales/ServiciosOpcionales.html'

class ServiciosOpcionalesDetailView(DetailView):
    model = ServiciosOpcionales
    template_name = "ServiciosOpcionales/ServiciosOpcionalesDetalle.html"

class ServiciosOpcionalesCreateView(CreateView):
    model = ServiciosOpcionales
    form_class = ServiciosOpcionalesForm
    template_name = 'ServiciosOpcionales/ServiciosOpcionalesForm.html'
    success_url = reverse_lazy("ServiciosOpcionalesList")

class ServiciosOpcionalesUpdateView(UpdateView):
    model = ServiciosOpcionales
    form_class = ServiciosOpcionalesForm
    template_name = 'ServiciosOpcionales/ServiciosOpcionalesForm.html'
    success_url = reverse_lazy("ServiciosOpcionalesList")

class ServiciosOpcionalesDeleteView(DeleteView):
    model = ServiciosOpcionales
    template_name = 'ServiciosOpcionales/ServiciosOpcionalesDeleteForm.html'
    success_url = reverse_lazy("ServiciosOpcionalesList")
#endregion

#region CRUD Lugar
class LugarListView(ListView):
    model = Lugar
    template_name = 'Lugar/Lugares.html'

class LugarDetailView(DetailView):
    model = Lugar
    template_name = "Lugar/LugarDetalle.html"

class LugarCreateView(CreateView):
    model = Lugar
    form_class = LugarForm
    template_name = 'Lugar/LugarForm.html'
    success_url = reverse_lazy("LugarList")

class LugarUpdateView(UpdateView):
    model = Lugar
    form_class = LugarForm
    template_name = 'Lugar/LugarForm.html'
    success_url = reverse_lazy("LugarList")

class LugarDeleteView(DeleteView):
    model = Lugar
    template_name = 'Lugar/LugarDeleteForm.html'
    success_url = reverse_lazy("LugarList")
#endregion

#region CRUD Evento
class EventoListView(ListView):
    model = Evento
    template_name = 'Evento/Eventos.html'

class EventoDetailView(DetailView):
    model = Evento
    template_name = "Evento/EventoDetalle.html"

class EventoCreateView(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'Evento/EventoForm.html'
    success_url = reverse_lazy("EventoList")

class EventoUpdateView(UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'Evento/EventoForm.html'
    success_url = reverse_lazy("EventoList")

class EventoDeleteView(DeleteView):
    model = Evento
    template_name = 'Evento/EventoDeleteForm.html'
    success_url = reverse_lazy("EventoList")

#endregion

#region CRUD ServiciosOpcionalesLista
class ServiciosOpcionalesListaListView(ListView):
    model = ServiciosOpcionalesLista
    template_name = 'ServiciosOpcionalesLista/ServiciosOpcionalesListas.html'

class ServiciosOpcionalesListaDetailView(DetailView):
    model = ServiciosOpcionalesLista
    template_name = "ServiciosOpcionalesLista/ServiciosOpcionalesListaDetalle.html"

class ServiciosOpcionalesListaCreateView(CreateView):
    model = ServiciosOpcionalesLista
    form_class = ServiciosOpcionalesListaForm
    template_name = 'ServiciosOpcionalesLista/ServiciosOpcionalesListaForm.html'
    success_url = reverse_lazy("ServiciosOpcionalesListaList")

class ServiciosOpcionalesListaUpdateView(UpdateView):
    model = ServiciosOpcionalesLista
    form_class = ServiciosOpcionalesListaForm
    template_name = 'ServiciosOpcionalesLista/ServiciosOpcionalesListaForm.html'
    success_url = reverse_lazy("ServiciosOpcionalesListaList")

class ServiciosOpcionalesListaDeleteView(DeleteView):
    model = ServiciosOpcionalesLista
    template_name = 'ServiciosOpcionalesLista/ServiciosOpcionalesListaDeleteForm.html'
    success_url = reverse_lazy("ServiciosOpcionalesListaList")
#endregion

#region CRUD ListadoMenus
class ListadoMenusListView(ListView):
    model = ListadoMenus
    template_name = 'ListadoMenus/ListadoMenus.html'

class ListadoMenusDetailView(DetailView):
    model = ListadoMenus
    template_name = "ListadoMenus/ListadoMenusDetalle.html"

class ListadoMenusCreateView(CreateView):
    model = ListadoMenus
    form_class = ListadoMenusForm
    template_name = 'ListadoMenus/ListadoMenusForm.html'
    success_url = reverse_lazy("ListadoMenusList")

class ListadoMenusUpdateView(UpdateView):
    model = ListadoMenus
    form_class = ListadoMenusForm
    template_name = 'ListadoMenus/ListadoMenusForm.html'
    success_url = reverse_lazy("ListadoMenusList")

class ListadoMenusDeleteView(DeleteView):
    model = ListadoMenus
    template_name = 'ListadoMenus/ListadoMenusDeleteForm.html'
    success_url = reverse_lazy("ListadoMenusList")
#endregion

