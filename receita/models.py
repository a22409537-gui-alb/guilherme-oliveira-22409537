from django.db import models

# Create your models here.
class Ingredientes(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Receita(models.Model):
    nome = models.CharField(max_length=20)
    ingredientes = models.ManyToManyField(Ingredientes, related_name='receitas')

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    receitas_fav = models.ManyToManyField(Receita, related_name='favoritas')

    def __str__(self):
        return self.nome