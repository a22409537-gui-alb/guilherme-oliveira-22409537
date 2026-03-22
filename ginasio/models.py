from django.db import models

# Create your models here.
class Ginasio(models.Model):
    nome = models.CharField(max_length=20)
    morada = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class PersonalTrainer(models.Model):
    nome = models.CharField(max_length=50)
    nr_registro = models.CharField(max_length=10)
    ginasio = models.ForeignKey(Ginasio, on_delete=models.CASCADE, related_name='pts')

    def __str__(self):
        return self.nome

class Membro(models.Model):
    nome = models.CharField(max_length=50)
    nr_registro = models.CharField(max_length=10)
    ginasio = models.ForeignKey(Ginasio, on_delete=models.CASCADE, related_name='alunos')

    def __str__(self):
        return self.nome

class Sessao(models.Model):
    data_hora = models.DateTimeField()
    aluno = models.ForeignKey(Membro, on_delete=models.SET_NULL, related_name='sessoes', null=True)
    personal = models.ForeignKey(PersonalTrainer, on_delete=models.SET_NULL, related_name='aulas', null=True)

    def __str__(self):
        return f'{self.personal.__str__}: {self.data_hora}'




