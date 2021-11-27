from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre=models.CharField(max_length=15,unique=True)
    contrasena=models.CharField(max_length=15)
    mail=models.EmailField(max_length=25)