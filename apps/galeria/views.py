from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.galeria.forms import FotografiaForms
from apps.galeria.models import Fotografia, Like
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    

    fotografias = Fotografia.objects.order_by('-data').filter(publicada=True)
    return render(request,'galeria/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request,'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("-data").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar'] # referencia a ao 'buscar' no html
        if nome_a_buscar: 
            fotografias = fotografias.filter(nome__icontains = nome_a_buscar) # nome__icontains irá buscar se, dentro do nome que estamos conferindo de um objeto em específico
        
    
    return render (request, "galeria/buscar.html", {"cards": fotografias})

def postar(request):
    if request.method == "POST":
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Postagem feita com sucesso")
            return redirect('index')
    else:
        # Filtre as opções de usuário apenas para o usuário logado
        form = FotografiaForms()
        

    return render(request, "galeria/postar.html", {'form': form})



def editar_postagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            print(request.POST)
            form.save()
            messages.success(request, 'Fotografia editada com sucesso')
            return redirect('index')
    return render(request, 'galeria/editar_postagem.html', {'form':form, 'foto_id': foto_id})

def deletar_postagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Postagem deletada!')
    return redirect('index')

def like_fotografia(request, fotografia_id):
    fotografia = get_object_or_404(Fotografia, pk=fotografia_id)
    user = request.user

    like, created = Like.objects.get_or_create(fotografia=fotografia, user=user)
    
    if created:
        messages.success(request, 'Você curtiu a fotografia!')
        if 1 < fotografia.likes_count  :
             fotografia.likes_count +=1 
             fotografia.save()
        else:
             fotografia.likes_count +=1
        fotografia.save()
    else:
        like.delete()
        messages.success(request, 'Você removeu o like da fotografia!')
        fotografia.likes_count -= 1
        fotografia.save()

    return redirect('imagem', foto_id=fotografia_id)