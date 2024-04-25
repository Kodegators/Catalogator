from django.db import models


# Create your models here.
class Generos(models.Model):
    genero = models.CharField('Nome', max_length=100)


class Itens(models.Model):
    nome = models.CharField('Nome', max_length=200)
    genero = models.ForeignKey(Generos, on_delete=models.PROTECT)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
