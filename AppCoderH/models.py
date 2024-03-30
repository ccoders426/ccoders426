from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"nombre: {self.nombre} camada: {self.camada}"

class Profesor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    celular = models.CharField(max_length=15)
    email = models.EmailField()
    curso = models.CharField(max_length=40)

    def __str__(self):
        return f"nombre: {self.nombre} apellido: {self.apellido} dni: {self.dni} celular: {self.celular} email: {self.email} curso: {self.curso}"
     
class Alumno(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    celular = models.CharField(max_length=15)
    email = models.EmailField()
    curso = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"nombre: {self.nombre} apellido: {self.apellido} dni: {self.dni} celular: {self.celular} email: {self.email} curso: {self.curso} camada: {self.camada}" 