from django.db import models


# Create your models here.

class Carro(models.Model):
    placa = models.CharField(max_length=10)
    nome = models.CharField(max_length=30)
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    ano_fabricacao = models.CharField(max_length=12)
    ano_modelo = models.CharField(max_length=12)
    cor = models.CharField(max_length=15)

    def __str__(self):
        return self.placa


class Cliente(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=13)
    endereco = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    nome_pai = models.CharField(max_length=30)
    nome_mae = models.CharField(max_length=30)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Vendedor(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=30)
    salario = models.IntegerField()
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=13)
    endereco = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    cnpj = models.CharField(max_length=20)
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=13)
    endereco = models.CharField(max_length=30)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Seguranca(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=13)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Vaga(models.Model):
    codigo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.codigo
