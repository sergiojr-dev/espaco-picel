from django.shortcuts import render, redirect
from apps.usuario.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth #biblioteca de autentificação do django



def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)

    if form.is_valid():
        
        nome =  form['nome_cadastro'].value()
        email = form['email'].value()
        senha = form['senha_1'].value()

        
        criar_usuario = User.objects.create_user(
             username = nome,
             password = senha,
             email = email
         )

        criar_usuario.save()
        messages.success(request, 'Cadastro criado com sucesso!')
        return redirect('login')

    return render(request, 'usuario/cadastro.html', {'form': form})

def login(request):
        form = LoginForms()
        if request.method == "POST":
            form = LoginForms(request.POST)
        
        if form.is_valid():
            nome = form["nome_login"].value()
            senha = form["senha"].value()
             
            usuario = auth.authenticate( # Essa variável será retornada como válida
                    request,
                    username=nome,
                    password=senha
             )
             
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'Seja Bem-vindo! {nome} ')
                return redirect ('index')

            else:
                messages.error(request, 'Erro ao efetuar login')
                return redirect('login')



           
        return render(request, "usuario/login.html", {"form": form})


def logout(request):
    auth.logout(request)
    messages.success(request , f"Você saiu da conta")
    
    return redirect('login')
