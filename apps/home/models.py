from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Cliente(models.Model):
    vagas = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)




class Estacionamentos(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    Data_cadastro = models.DateTimeField(auto_now_add=True)
    vagas = models.IntegerField()
    active = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='estacionamento')
    valor = models.FloatField(default=15.00)



    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "Estacionamentos"   

    
class Mapa(models.Model):
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)


    

