from django.contrib import admin

# Register your models here.
from .models import UnidadMedida, ConversionUnidad

admin.site.register(UnidadMedida)
admin.site.register(ConversionUnidad)