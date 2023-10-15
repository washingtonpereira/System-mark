from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Consulta(models.Model):
    titulo = models.CharField(max_length=22)
    descricao =models.TextField(blank=True, null=True)
    data_consulta =models.DateField(verbose_name="Data da Consulta")
    data_criacao = models.DateField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    

    
    def __str__(self):
        return self.titulo