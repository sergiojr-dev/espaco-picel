from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.galeria.forms import fotografiaForms
from apps.galeria.models import Fotografia
from django.contrib.auth.models import User
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
        form = fotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Postagem feita com sucesso")
            return redirect('index')
    else:
        # Filtre as opções de usuário apenas para o usuário logado
        form = fotografiaForms()
        form.fields['usuario'].queryset = User.objects.filter(pk=request.user.pk)

    return render(request, "galeria/postar.html", {'form': form})