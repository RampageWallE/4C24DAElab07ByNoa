from django.db import models

# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    fechainicio = models.DateTimeField()
    fechafin = models.DateTimeField()
    fecha_registro = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=12)
    CLASE_CHOICE = [
        ("admin", "admin"),
        ("clien", "clien")
    ]
    clase = models.CharField(max_length=5, choices=CLASE_CHOICE)
    dni = models.BigIntegerField()
    email = models.EmailField()
    fecha_registro = models.DateTimeField('date published', auto_now=True)
    
    def __str__(self):
        return self.nombre

class RegistroEvento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField('fecha de registro', auto_now=True)

    def __date__(self):
        return self.fecha_registro
    