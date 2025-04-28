from django.db import models


class Motocicleta(models.Model):
    fecha_creacion = models.DateField(null=True)
    marca = models.CharField(max_length=100)
    linea = models.CharField(max_length=100)
    modelo = models.IntegerField()
    placa = models.CharField(max_length=100)
    chasis = models.CharField(max_length=100)
    motor = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.placa} - {self.marca} - {self.linea} - {self.modelo} - {self.chasis} - {self.motor} - {self.precio}'

