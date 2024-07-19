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

class MenuForm(models.ModelForm):
    class Meta:
        model = Menu
        fields = ("nombreOficial", "descripcion",)

class RecetaForm(models.ModelForm):
    class Meta:
        model = Receta
        fields = ("codigoReceta", "nombreReceta", "idOrigen", "noPorciones", "temperaturaServicio", "tiempoElab", "costoReceta", "precioVenta",)

class TecnicasRecetaForm(models.ModelForm):
    class Meta:
        model = TecnicasReceta
        fields = ("recetaId", "tecnicaID",)

class IngredientesRecetaForm(models.ModelForm):
    class Meta:
        model = IngredientesReceta
        fields = ("ingredienteId", "cantidadUso", "medidaUso", "rendimiento", "recetaID", )

class RecetaCostosForm(models.ModelForm):
    class Meta: 
        model = RecetaCostos
        fields = ("ingredientesRecetaID", "recetaId",)

class MenuRecetasForm(models.ModelForm):
    class Meta:
        model = MenuRecetas
        fields = ("recetaId", "menuId",)

class ClienteForm:
    class Meta:
        model = Cliente
        fields = ("nombres", "apellidos", "nit","telefono", "email",)

class ServiciosOpcionalesForm(models.ModelForm):
    class Meta:
        model = ServiciosOpcionales
        fields = ("servicio", "precioUnitario", "detalles")

class LugarForm(models.ModelForm):
    class Meta:
        model = Lugar
        fields = ("nombre", "minPersonas", "maxPersonas", "ubicacion", "detalles",)

class EventoForm(models.ModelForm):
    class Meta:
        model = Evento
        fields = ("nombre", "codigo", "clienteID", "lugarID", "fecha","horaInicio", "horaFin", "isCotizacion", "cantPersonas")

class ServiciosOpcionalesListaForm(models.ModelForm):
    class Meta:
        model = ServiciosOpcionalesLista
        fields = ("servOpID", "eventoID", "observaciones")

class ListadoMenusForm(models.ModelForm):
    class Meta: 
        model = ListadoMenus
        fields = ("menuID", "cantidad", "observaciones", "eventoID")



