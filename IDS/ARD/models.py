from django.db import models

#RAZAS = [('DOBERMAN','dobermas'),('OBEJERO','Objero Aleman')]

# Create your models here.
class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.IntegerField()
    skill = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

