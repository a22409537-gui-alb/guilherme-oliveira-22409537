from django.db import models

# Create your models here.
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
    
class Turma(models.Model):
    nr = models.CharField(max_length=5)
    professor = models.OneToOneField(Professor, on_delete=models.CASCADE, related_name='turma')
    alunos = models.ForeignKey(Aluno,on_delete=models.CASCADE, related_name='turma')
    
    def __str__(self):
        return f'Turma: {self.__str__}'


class Escola(models.Model):
    nome = models.CharField(max_length=100)
    morada = models.CharField(max_length=100)
    turmas = models.ForeignKey(Turma,on_delete=models.CASCADE, related_name='escola')

    def __str__(self):
        return self.nome