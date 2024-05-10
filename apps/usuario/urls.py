from django.urls import path
from apps.usuario.views import cadastro, login,logout, editar_usuario

urlpatterns= [
    path ('cadastro',cadastro, name = 'cadastro'),
    path('login',login, name = 'login'),
    path ('logout', logout , name ='logout'),
    path('editar_usuario/<int:user_id>/', editar_usuario, name='editar_usuario'),
]
    
    
