from django.urls import path
from usuario.views import cadastro, login,logout

urlpatterns= [
    path ('cadastro',cadastro, name = 'cadastro'),
    path('login',login, name = 'login'),
    path ('logout', logout , name ='logout')
]
    
    
