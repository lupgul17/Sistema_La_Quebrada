from django.db import models
from django.conf import settings
# Create your models here.

#region Menu
#*************INICIO DEL MÓDULO DE MENÚ************************ s

class UnidadMedida(models.Model):
    idUnidadMedida = models.AutoField(primary_key=True)
    unidad = models.CharField(max_length=255, blank=False, null=False, error_messages="El campo no puede estar vacío") 
    def __str__(self):
        return self.unidad
    
class ConversionUnidad(models.Model):
    idConversion = models.AutoField(primary_key=True)
    unidadOrigen = models.ForeignKey(UnidadMedida, related_name='unidad_origen', on_delete=models.CASCADE)
    unidadDestino = models.ForeignKey(UnidadMedida, related_name='unidad_destino', on_delete=models.CASCADE)
    factorConversion = models.DecimalField(max_digits=10, decimal_places=6, help_text="Factor de conversión de origen a destino")
    
    def __str__(self):
        return f"{self.unidadOrigen} -> {self.unidadDestino}: {self.factorConversion}"

class Ingrediente(models.Model):
    idIngrediente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    unidadCompra = models.IntegerField()
    idUnidadMedida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    precioUnidadCompra = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    especificaciones = models.TextField(blank=True, null=True)
    existencias = models.IntegerField()
    def __str__(self):
        return self.nombre

class TecnicaCoccion(models.Model):
    idTecnicaCoccion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    

class Origen(models.Model):
    idOrigen = models.AutoField(primary_key=True)
    origen = models.CharField(max_length=255)

    def __str__(self):
        return self.origen

class Menu(models.Model):
    idMenu = models.AutoField(primary_key=True)
    nombreOficial = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombreOficial

class Receta(models.Model):
    OPCIONES = (("Frio", "Frio"), ("Caliente", "Caliente"), ("Al tiempo", "Al Tiempo"))
    idReceta = models.AutoField(primary_key=True)
    codigoReceta = models.CharField(max_length=255)
    nombreReceta = models.CharField(max_length=255)
    idOrigen = models.ForeignKey(Origen, on_delete=models.CASCADE)
    noPorciones = models.IntegerField()
    temperaturaServicio = models.CharField(max_length=10, choices=OPCIONES, default="Caliente")
    tiempoElab = models.CharField(max_length=100)
    costoReceta = models.DecimalField(max_digits=10, decimal_places=2)
    precioSugerido = models.DecimalField(max_digits=10, decimal_places=2)
    precioVenta = models.DecimalField(max_digits=10, decimal_places=2)
    procedimiento = models.TextField()
    def __str__(self):
        return self.nombreReceta

class TecnicasReceta(models.Model):
    idTecnicasReceta = models.AutoField(primary_key=True)
    recetaId = models.ForeignKey(Receta, on_delete=models.CASCADE)
    tecnicaID = models.ForeignKey(TecnicaCoccion, on_delete=models.CASCADE)
    detalles = models.TextField()
    def __str__(self):
        return self.idTecnicasReceta

class IngredientesReceta(models.Model):
    idIngredientesReceta = models.AutoField(primary_key=True)
    ingredienteId = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    cantidadUso = models.IntegerField()
    medidaUso = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    rendimiento = models.IntegerField()
    recetaID = models.ForeignKey(Receta, on_delete=models.CASCADE)
    def __str__(self):
        return self.idIngredientesReceta

class RecetaCostos(models.Model):
    idRecetaCostos = models.AutoField(primary_key=True)
    ingredientesRecetaID = models.ForeignKey(IngredientesReceta, on_delete=models.CASCADE)
    recetaId = models.ForeignKey(Receta, on_delete=models.CASCADE)

    def __str__(self):
        return self.idRecetaCostos
    
class MenuRecetas(models.Model):
    idMenuRecetas = models.AutoField(primary_key=True)
    recetaId = models.ForeignKey(Receta, on_delete=models.CASCADE)
    menuId = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.idMenuRecetas
#endregion

#region Clientes
class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=255, blank=False, null=False)
    apellidos = models.CharField(max_length=255, blank=False, null=False)
    nit = models.CharField(max_length=20)
    telefono = models.CharField(max_length=8)
    email = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombres + self.apellidos
#endregion

#region Evento
#------------ SECCION EVENTOS --------------
class ServiciosOpcionales(models.Model):
    idServOp = models.AutoField(primary_key=True)
    servicio = models.CharField(max_length=255)
    precioUnitario = models.DecimalField(max_digits=10, decimal_places=2)
    detalles = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.servicio

class Lugar(models.Model):
    idLugar = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    minPersonas = models.IntegerField()
    maxPersonas = models.IntegerField()
    ubicacion = models.CharField(max_length=255)
    detalles = models.TextField()

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    idEvento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)
    clienteID = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    lugarID = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    fecha = models.DateField()
    horaInicio = models.TimeField()
    horaFin = models.TimeField()
    isCotizacion = models.BooleanField()
    cantPersonas = models.IntegerField()

    def __str__(self):
        return self.nombre
    

class ServiciosOpcionalesLista(models.Model):
    idServOpList= models.AutoField(primary_key = True)
    servOpID = models.ForeignKey(ServiciosOpcionales, on_delete=models.CASCADE)
    eventoID = models.ForeignKey(Evento, on_delete=models.CASCADE)
    observaciones = models.TextField()

    def __str__(self):
        return self.servOpListID
    

class ListadoMenus(models.Model):
    idListMenu = models.AutoField(primary_key=True)
    menuID = models.ForeignKey(Menu, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    observaciones = models.TextField()
    eventoID = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return self.listMenuID


#endregion

