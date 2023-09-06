from django.contrib import admin
from galeria.models import Fotografia


class CadastroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada') # aparecer os atributos dentro do admin
    list_display_links = ('id', 'nome') # colocar o link dentro dos atributos do adin
    search_fields = ('nome', 'categoria') # campo de busca dentro do admin do django
    list_filter = ('categoria',) # esta fazendo um filtro por categoria dentro do admin
    list_editable = ('publicada',) #da a opção de publicar ou despublicar direto no admin
    list_per_page = 10 # quantidade de itens por página

# Register your models here.
admin.site.register(Fotografia, CadastroAdmin)