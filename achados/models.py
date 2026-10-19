from django.db import models


class Objeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    local = models.CharField(max_length=200)
    data = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.nome