from django.db import models

# Create your models here.
class Escola(models.Model):
    nome = models.CharField(max_length=100)
    morada = models.CharField(max_length=100)

class Turma(models.Model):
    nr = models.CharField(max_length=5)
    
class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    nr = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome
    