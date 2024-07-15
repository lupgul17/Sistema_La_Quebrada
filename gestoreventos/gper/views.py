from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PostUnidadMedida, PostIngrediente
from .models import UnidadMedida, Ingrediente

# Create your views here.
def index(request):
    return HttpResponse("Hola Mundo xD")

#region CRUD UnidadMedida
# def UnidadMedidaList(request):
#     unidades = UnidadMedida.objects.all()
#     return render(request, 'gper/Unidades.html', {'unidades': unidades})

# def UnidadMedidaNew(request):
#     if request.method == "POST":
#         form = PostUnidadMedida(request.POST)
#         if form.is_valid():
#             unidadmedida = form.save(commit=False)
#             unidadmedida.save()
#             return redirect("UM")
#     else:
#         form = PostUnidadMedida()
#     return render(request, 'gper/UnidadMedidaEdit.html', {'form':form})
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

