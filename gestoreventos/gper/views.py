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
# def IngredienteList(request):
#     ingredientes = Ingrediente.objects.all()
#     return render(request, 'gper/Ingredientes.html', {'ingredientes':ingredientes})

# def IngredienteNew(request):
#     if request.method == "POST":
#         form = PostIngrediente(request.POST)
#         if form.is_valid():
#             ingrediente = form.save(commit=False)
#             ingrediente.save()
#             return redirect("Ingrediente")
#endregion

