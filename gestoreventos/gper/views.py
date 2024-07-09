from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostUnidadMedida

# Create your views here.
def index(request):
    return HttpResponse("Hola Mundo xD")

def UnidadMedidaNew(request):
    form = PostUnidadMedida()
    return render(request, 'gper/UnidadMedidaEdit.html', {'form':form})
