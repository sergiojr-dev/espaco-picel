from django.db import models
from django.contrib.auth.models import User
from apps.galeria.models import Fotografia

class Comentario(models.Model):
    post1  = models.ForeignKey(Fotografia,on_delete=models.CASCADE)
    
    usuario = models.ForeignKey(
        to = User,
        on_delete = models.SET_NULL,          # caso o usuario for deletado como sera defido no null
        null= True,
        blank= False,
        related_name= 'user_comentario',                  #  e para facilitar a localização de tabelas e funcionalidades
    )
    comment = models.TextField(null=False, blank=False)

    data_comentario = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.comment
