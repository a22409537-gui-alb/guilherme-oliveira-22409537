from django.db import models

# Create your models here.
class Genero(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Banda(models.Model):
    nome = models.CharField(max_length=50)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, related_name='bandas', null=True)

    def __str__(self):
        return self.nome

class Festival(models.Model):
    nome = models.CharField(max_length=50)
    data = models.DateField()
    bandas = models.ManyToManyField(Banda, related_name="festivais")

    def __str__(self):
        return self.nome