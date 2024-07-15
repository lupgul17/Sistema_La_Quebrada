from django import forms    
from .models import UnidadMedida, Ingrediente

class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ("unidad",)

class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ("nombre", "unidadCompra", "idUnidadMedida", "precioUnidadCompra", "especificaciones",)

