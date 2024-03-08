from django.urls import path
from apps.comentario.views import criar_comentario
from . import views

urlpatterns= [
    path("criar_comentario/<int:foto_id>", criar_comentario, name = 'criar_comentario' ),
    path('lista_comentarios/<int:foto_id>/', views.lista_comentarios, name='lista_comentarios'),
]



