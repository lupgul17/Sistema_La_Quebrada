from django import forms    
from .models import *

class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ("unidad",)
    def __init__(self, *args, **kwargs):
        super(UnidadMedidaForm, self).__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ("nombre", "unidadCompra", "idUnidadMedida", "precioUnidadCompra", "especificaciones","existencias",)
    def __init__(self, *args, **kwargs):
        super(IngredienteForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class TecnicaCoccionForm(forms.ModelForm):
    class Meta: 
        model = TecnicaCoccion
        fields = ("nombre", "descripcion",)
    def __init__(self, *args, **kwargs):
        super(TecnicaCoccionForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class OrigenForm(forms.ModelForm):
    class Meta:
        model = Origen
        fields = ("origen",)
    def __init__(self, *args, **kwargs):
        super(OrigenForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ("nombreOficial", "descripcion",)

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ("codigoReceta", "nombreReceta", "idOrigen", "noPorciones", "temperaturaServicio", "tiempoElab","procedimiento")

class TecnicasRecetaForm(forms.ModelForm):
    class Meta:
        model = TecnicasReceta
        fields = ("recetaId", "tecnicaID","detalles")

class IngredientesRecetaForm(forms.ModelForm):
    class Meta:
        model = IngredientesReceta
        fields = ("ingredienteId", "cantidadUso", "medidaUso", "rendimiento", "recetaID", )
    def __init__(self, *args, **kwargs):
        ingrediente = kwargs.pop('ingrediente', None)
        super().__init__(*args, **kwargs)
        if ingrediente:
            self.fields['medidaUso'].queryset = UnidadMedida.objects.filter(unidad_destino__unidadOrigen=ingrediente.idUnidadMedida)

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

