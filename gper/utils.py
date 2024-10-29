# utils.py
from decimal import Decimal
from .models import ConversionUnidad

def convertir_unidad(cantidad, unidad_origen, unidad_destino):
    try:
        conversion = ConversionUnidad.objects.get(unidadOrigen=unidad_origen, unidadDestino=unidad_destino)
        return cantidad * conversion.factorConversion
    except ConversionUnidad.DoesNotExist:
        # Manejar el caso donde no exista la conversión específica
        raise ValueError(f"No se encontró conversión de {unidad_origen} a {unidad_destino}")
