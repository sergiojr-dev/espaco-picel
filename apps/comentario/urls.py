from django.urls import path
from apps.comentario.views import criar_comentario , lista_comentarios, editar_comentario, deletar_comentario

urlpatterns= [
    path("criar_comentario/<int:foto_id>", criar_comentario, name = 'criar_comentario' ),
    path('lista_comentarios/<int:foto_id>/', lista_comentarios, name='lista_comentarios'),
    path('editar_comentario/<int:comentario_id>/', editar_comentario, name='editar_comentario'),
    path('deletar_comentario/<int:comentario_id>/', deletar_comentario, name='deletar_comentario')
    ]



