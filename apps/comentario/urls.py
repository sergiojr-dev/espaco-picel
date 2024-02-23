from django.urls import path
from apps.comentario.views import criar_comentario


urlpatterns= [
    path("criar_comentario/<int:foto_id>", criar_comentario, name = 'criar_comentario' ),
]

