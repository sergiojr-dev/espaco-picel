from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
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
    categoria = models.CharField(max_length=50, choices=OPCOES_CATEGORIAS, default='') #choice serve para dizer que serão categorias pré definidas e selecionaveis e default para dizer em qual ela inicia
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=True)
    data = models.DateTimeField(auto_now_add=True, blank=False)
    usuario = models.ForeignKey(
        to = User,
        on_delete = models.SET_NULL,          # caso o usuario for deletado como sera defido no null
        null= True,
        blank= False,
        related_name= 'user',                  #  e para facilitar a localização de tabelas e funcionalidades
    )

    likes_count = models.IntegerField(default= 0)



    def __str__(self):
        return self.nome
    
class Like(models.Model):
    fotografia = models.ForeignKey(Fotografia, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('fotografia', 'user',)

    def __str__(self):
        return f'{self.user.username} likes {self.fotografia.nome}'