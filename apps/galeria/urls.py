from django.urls import path
from apps.galeria.views import index, imagem, buscar, postar, editar_postagem, deletar_postagem,like_fotografia


urlpatterns= [
    path('',index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path("buscar", buscar, name = 'buscar' ),
    path("postar", postar, name = 'postar' ),
    path('editar-postagem/<int:foto_id>', editar_postagem, name='editar_postagem'),
    path('deletar-postagem/<int:foto_id>', deletar_postagem, name='deletar_postagem'),
    path('fotografia/<int:fotografia_id>/like/', like_fotografia, name='like_fotografia'),
]


