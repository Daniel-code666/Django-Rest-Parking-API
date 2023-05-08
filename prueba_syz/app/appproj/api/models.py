from django.db import models

# Create your models here.
class Conductores(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    licencia_conducir = models.CharField(max_length=20)
    fecha_vencimiento_licencia = models.DateField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'conductores'