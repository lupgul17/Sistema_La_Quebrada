from django import forms    
from .models import UnidadMedida

class PostUnidadMedida(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ("unidad",)

