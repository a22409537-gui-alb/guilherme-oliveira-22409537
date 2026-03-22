from django.db import models

# Create your models here.
class Loja(models.Model):
    nome = models.CharField(max_length=50)
    morada = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    loja = models.ForeignKey(Loja,on_delete=models.CASCADE, related_name='produtos')
    categoria = models.ForeignKey(Categoria,on_delete=models.SET_NULL, related_name='produtos', null=True)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    total = models.IntegerField()
    def __str__(self):
        return f'Pedido: {self.id}, total: {(self.total/100)}'
    

class Item(models.Model):
    quantidade = models.IntegerField()
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE, related_name='items')
    pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f'{self.produto}: {self.quantidade}'

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    morada = models.CharField(max_length=50)
    email = models.EmailField()

    pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE, related_name='consumidor')

    def __str__(self):
        return self.nome
    