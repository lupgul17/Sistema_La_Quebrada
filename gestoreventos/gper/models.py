from django.db import models

# Create your models here.

#region Menu
#*************INICIO DEL MÓDULO DE MENÚ************************

class UnidadMedida(models.Model):
    idUnidadMedida = models.AutoField(primary_key=True)
    unidad = models.CharField(max_length=255)

    def __str__(self):
        return self.unidad
    
class Ingrediente(models.Model):
    idIngrediente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    unidadCompra = models.IntegerField()
    idUnidadMedida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    precioUnidadCompra = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    especificaciones = models.TextField(blank=True, null=True)

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
    OPCIONES = (("frio", "Frio"), ("caliente", "Caliente"), ("al tiempo", "Al Tiempo"))
    idReceta = models.AutoField(primary_key=True)
    codigoReceta = models.CharField(max_length=255)
    nombreReceta = models.CharField(max_length=255)
    idOrigen = models.ForeignKey(Origen, on_delete=models.CASCADE)
    noPorciones = models.IntegerField()
    temperaturaServicio = models.CharField(max_length=10, choices=OPCIONES, default="caliente")
    tiempoElab = models.CharField(max_length=100)
    costoReceta = models.DecimalField(max_digits=10, decimal_places=2)
    precioVenta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombreReceta

class TecnicasReceta(models.Model):
    idTecnicasReceta = models.AutoField(primary_key=True)
    recetaId = models.ForeignKey(Receta, on_delete=models.CASCADE)
    tecnicaID = models.ForeignKey(TecnicaCoccion, on_delete=models.CASCADE)
    
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
