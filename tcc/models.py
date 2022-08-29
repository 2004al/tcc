from django.db import models


class Autor(models.Model):
    primero_nome = models.CharField(max_length=100)
    ultimo_nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/')


def __str__(self):
    return self.nome


class Orientador(models.Model):
    primero_nome = models.CharField(max_length=100)
    ultimo_nome = models.CharField(max_length=100)


def __str__(self):
    return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    modalidade = models.CharField(max_length=100,)
    bacharelado = models.CharField(verbose_name="bacharelado")
    licenciatura = models.IntegerField(verbose_name="licenciatura")
    tecnológico = models.IntegerField(verbose_name="tecnológico")

def __str__(self):
    return self.nome
