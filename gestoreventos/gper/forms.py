from django import forms    
from .models import *

class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ("unidad",)

class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ("nombre", "unidadCompra", "idUnidadMedida", "precioUnidadCompra", "especificaciones",)

class TecnicaCoccionForm(forms.ModelForm):
    class Meta: 
        model = TecnicaCoccion
        fields = ("nombre", "descripcion",)

class OrigenForm(forms.ModelForm):
    class Meta:
        model = Origen
        fields = ("origen",)

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ("nombreOficial", "descripcion",)

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ("codigoReceta", "nombreReceta", "idOrigen", "noPorciones", "temperaturaServicio", "tiempoElab", "costoReceta", "precioVenta",)

class TecnicasRecetaForm(forms.ModelForm):
    class Meta:
        model = TecnicasReceta
        fields = ("recetaId", "tecnicaID",)

class IngredientesRecetaForm(forms.ModelForm):
    class Meta:
        model = IngredientesReceta
        fields = ("ingredienteId", "cantidadUso", "medidaUso", "rendimiento", "recetaID", )

class RecetaCostosForm(forms.ModelForm):
    class Meta: 
        model = RecetaCostos
        fields = ("ingredientesRecetaID", "recetaId",)

class MenuRecetasForm(forms.ModelForm):
    class Meta:
        model = MenuRecetas
        fields = ("recetaId", "menuId",)

class ClienteForm:
    class Meta:
        model = Cliente
        fields = ("nombres", "apellidos", "nit","telefono", "email",)

class ServiciosOpcionalesForm(forms.ModelForm):
    class Meta:
        model = ServiciosOpcionales
        fields = ("servicio", "precioUnitario", "detalles")

class LugarForm(forms.ModelForm):
    class Meta:
        model = Lugar
        fields = ("nombre", "minPersonas", "maxPersonas", "ubicacion", "detalles",)

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ("nombre", "codigo", "clienteID", "lugarID", "fecha","horaInicio", "horaFin", "isCotizacion", "cantPersonas")

class ServiciosOpcionalesListaForm(forms.ModelForm):
    class Meta:
        model = ServiciosOpcionalesLista
        fields = ("servOpID", "eventoID", "observaciones")

class ListadoMenusForm(forms.ModelForm):
    class Meta: 
        model = ListadoMenus
        fields = ("menuID", "cantidad", "observaciones", "eventoID")



