from django.contrib import admin
from apps.comentario.models import Comentario

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'usuario', 'data_comentario')

admin.site.register(Comentario, CommentAdmin)

