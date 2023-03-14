from django.db import models

class fomularioModel(models.Model):
    titolo = models.CharField(max_length=23)
    decricao = models.CharField(max_length=166)
    link = models.CharField(max_length=300)
    imagem = models.CharField(max_length=300)
