from django.db import models
from datetime import datetime

# Create your models here.
class Fotografia(models.Model):

    OPCOES_CATEGORIAS = [ # serve para criar e deixar as categorias pré definidas
        ("NEBULOSA", 'Nebulosa'),
        ("ESTRELA", 'Estrela'),
        ("GALÁXIA", 'Galáxia'),
        ("PLANETA", 'Planeta')
    ]

    nome = models.CharField(max_length=60, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=50, choices=OPCOES_CATEGORIAS, default='')
    #choice serve para dizer que serão categorias pré definidas e selecionaveis e default para dizer em qual ela inicia
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    publicada = models.BooleanField(default=False)
    data = models.DateTimeField(default=datetime.now, blank=False)


    def __str__(self):
        return f'Fotografia [nome={self.nome}]'